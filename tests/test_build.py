"""Mechanical traceability and generated-site regression checks."""

from __future__ import annotations

import json
import re
from pathlib import Path

from scripts import build_site
from scripts.build_site import LAZYALPHA_ROOT, SITE_ROOT


REPORTS_DIR = LAZYALPHA_ROOT / "reports"
SOURCE_REPORT_RE = re.compile(r"^\*\*Source report:\*\* `([^`]+)`", re.MULTILINE)
VARIANT_RE = re.compile(
    r"^### Variant (\d+) \{:\s*#(variant-\d+)\s*\}\s*$\n?"
    r"(.*?)(?=^### Variant \d+ \{:\s*#variant-\d+\s*\}\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)
BADGE_RE = re.compile(
    r'<span class="verdict-badge ([^"]+)">([^<]+)</span>'
)


def _read(path: Path) -> str:
    """Read UTF-8 while normalizing newlines for cross-platform comparisons."""
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def _is_numeric_cell(cell: str) -> bool:
    candidate = cell.strip().replace(",", "")
    if candidate.endswith("%"):
        candidate = candidate[:-1]
    try:
        float(candidate)
    except ValueError:
        return False
    return bool(candidate)


def _metric_sections(variant_text: str) -> list[str]:
    pattern = re.compile(
        r"^#### (?:Net backtest metrics|Available comparator metrics)[^\n]*\n"
        r"(.*?)(?=^#### |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.findall(variant_text)


def _badge(text: str) -> tuple[str, str]:
    match = BADGE_RE.search(text)
    assert match is not None, "expected a verdict badge"
    return match.group(1), match.group(2)


def test_every_model_card_metric_traces_to_source() -> None:
    model_paths = sorted((SITE_ROOT / "docs" / "models").glob("*.md"))
    assert model_paths, "no generated model cards found"

    variants_checked = 0
    metrics_checked = 0
    verdicts_checked = 0
    for model_path in model_paths:
        page = _read(model_path)
        variants = list(VARIANT_RE.finditer(page))
        assert variants, f"{model_path.name}: no variant sections found"
        for variant in variants:
            variant_text = variant.group(3)
            source_match = SOURCE_REPORT_RE.search(variant_text)
            assert source_match is not None, (
                f"{model_path.name}#{variant.group(2)}: missing Source report"
            )
            source_path = REPORTS_DIR / source_match.group(1)
            assert source_path.is_file(), f"referenced source report does not exist: {source_path}"
            source = _read(source_path)

            sections = _metric_sections(variant_text)
            assert sections, f"{model_path.name}#{variant.group(2)}: no metric section found"
            for section in sections:
                for line in section.splitlines():
                    stripped = line.strip()
                    if not (stripped.startswith("|") and stripped.endswith("|")):
                        continue
                    for cell in (part.strip() for part in stripped[1:-1].split("|")):
                        if _is_numeric_cell(cell):
                            assert cell in source, (
                                f"{model_path.name}#{variant.group(2)}: metric {cell!r} "
                                f"is not verbatim in {source_path.name}"
                            )
                            metrics_checked += 1

            rendered_sections = variant_text[variant_text.index("#### ") :]
            bold_lines = re.findall(r"^\*\*.+\*\*\s*$", rendered_sections, re.MULTILINE)
            for verdict in bold_lines:
                verdict = verdict.rstrip()
                assert verdict in source, (
                    f"{model_path.name}#{variant.group(2)}: verdict {verdict!r} "
                    f"is not verbatim in {source_path.name}"
                )
                verdicts_checked += 1
            variants_checked += 1

    assert variants_checked > 0
    assert metrics_checked > 0
    assert verdicts_checked > 0


def test_every_research_note_body_traces_to_source() -> None:
    note_paths = sorted((SITE_ROOT / "docs" / "notes").glob("*.md"))
    assert note_paths, "no generated research notes found"
    source_reports = {path.name: _read(path) for path in REPORTS_DIR.glob("*.md")}
    assert source_reports, "no LazyAlpha source reports found"

    rows_checked = 0
    for note_path in note_paths:
        note = _read(note_path)
        generated = re.search(r"^\*\*Generated:\*\*.*$", note, re.MULTILINE)
        assert generated is not None, f"{note_path.name}: missing generated metadata"
        remainder = note[generated.end() :]
        first_content = re.search(r"\S", remainder)
        assert first_content is not None, f"{note_path.name}: empty note body"
        body = remainder[first_content.start() :]

        matching_sources = [name for name, source in source_reports.items() if body in source]
        assert matching_sources, (
            f"{note_path.name}: rendered body is not a verbatim substring of any source report"
        )

        table_rows = [
            line.strip()
            for line in body.splitlines()
            if line.strip().startswith("|") and line.strip().endswith("|")
        ]
        for row in table_rows:
            assert any(row in source_reports[name] for name in matching_sources), (
                f"{note_path.name}: table row {row!r} is not in its source report"
            )
            rows_checked += 1

    assert rows_checked > 0, "research notes contained no markdown table rows"


def test_chart_images_reserve_layout_space() -> None:
    """Charts must have dimensions before their SVG payload finishes decoding."""
    pages = [SITE_ROOT / "docs" / "index.md", SITE_ROOT / "docs" / "leaderboard.md"]
    pages.extend(sorted((SITE_ROOT / "docs" / "models").glob("*.md")))
    image_tags = []
    for page in pages:
        image_tags.extend(
            re.findall(r'<figure class="[^"]*la-chart[^"]*".*?<img ([^>]+)>', _read(page), re.DOTALL)
        )

    assert image_tags, "no generated chart images found"
    for attributes in image_tags:
        assert 'width="576"' in attributes
        assert 'height="241"' in attributes
        assert 'loading="lazy"' not in attributes

    css = _read(SITE_ROOT / "docs" / "stylesheets" / "extra.css")
    assert "aspect-ratio: 160 / 67" in css
    assert ".la-chart img { display: block; width: 100%; max-width: 100%; height: auto;" in css


def test_leaderboard_badges_match_model_card_badges() -> None:
    leaderboard = _read(SITE_ROOT / "docs" / "leaderboard.md")
    card_re = re.compile(
        r'<article class="la-result-card [^"]+" data-model="([^"]+)" '
        r'data-variant="(variant-\d+)">(.*?)</article>',
        re.DOTALL,
    )
    cards = list(card_re.finditer(leaderboard))
    assert cards, "leaderboard contained no model variant cards"

    for card in cards:
        model_slug, anchor, card_html = card.groups()
        model_page = _read(SITE_ROOT / "docs" / "models" / f"{model_slug}.md")
        variant = next(
            (match.group(3) for match in VARIANT_RE.finditer(model_page) if match.group(2) == anchor),
            None,
        )
        assert variant is not None, f"{model_slug}#{anchor}: linked variant anchor not found"
        assert _badge(card_html) == _badge(variant), (
            f"{model_slug}#{anchor}: leaderboard and model-card badges differ"
        )


def test_charts_are_discoverable_and_truthfully_labeled() -> None:
    leaderboard = _read(SITE_ROOT / "docs" / "leaderboard.md")
    homepage = _read(SITE_ROOT / "docs" / "index.md")
    dataset = json.loads(_read(SITE_ROOT / "data" / "experiments.generated.json"))
    variants = [
        variant
        for family in dataset["families"].values()
        for variant in family["variants"]
    ]

    assert leaderboard.count('<article class="la-result-card ') == len(variants)
    assert leaderboard.count("<img ") == len(variants)
    equity_count = sum(variant["equity_companion_found"] for variant in variants)
    fallback_count = len(variants) - equity_count
    assert leaderboard.count('data-chart-kind="equity"') == equity_count
    assert leaderboard.count('data-chart-kind="fallback"') == fallback_count
    assert leaderboard.count("No equity time series available for this run") == fallback_count

    passes = [variant for variant in variants if variant["verdict_category"] == "pass"]
    assert homepage.count('<article class="la-featured-card">') == len(passes)
    assert homepage.count('data-chart-kind="equity"') == len(passes)

    for variant in variants:
        model_page = _read(SITE_ROOT / "docs" / "models" / f"{variant['slug']}.md")
        section = next(
            match.group(3)
            for match in VARIANT_RE.finditer(model_page)
            if match.group(2) == f"variant-{variant['variant_index']}"
        )
        assert section.index('<figure class="la-chart') < section.index("**Generated:**")
        assert section.index('<figure class="la-chart') < section.index("#### Experiment")
        expected_kind = "equity" if variant["equity_companion_found"] else "fallback"
        assert f'data-chart-kind="{expected_kind}"' in section


def test_research_terminal_theme_tokens_are_present() -> None:
    css = _read(SITE_ROOT / "docs" / "stylesheets" / "extra.css")
    for token in (
        "--la-bg: #080d14",
        "--la-green: #69e6a6",
        ".la-result-card",
        ".la-chart--fallback",
    ):
        assert token in css


def test_generator_exits_zero_on_current_state() -> None:
    build_site.build()
