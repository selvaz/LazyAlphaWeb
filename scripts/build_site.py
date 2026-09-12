"""Build the LazyAlpha research site from the source repository's reports."""

from __future__ import annotations

import html
import io
import json
import ntpath
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


LAZYALPHA_ROOT = Path(r"C:\Users\Administrator\Documents\GitHub\LazyAlpha")
SITE_ROOT = Path(__file__).resolve().parent.parent

REPORTS_DIR = LAZYALPHA_ROOT / "reports"
REGISTRY_PATH = LAZYALPHA_ROOT / "lazyalpha" / "state" / "experiments.jsonl"
DOCS_DIR = SITE_ROOT / "docs"
MODELS_DIR = DOCS_DIR / "models"
NOTES_DIR = DOCS_DIR / "notes"
CHARTS_DIR = DOCS_DIR / "assets" / "charts"
DATA_DIR = SITE_ROOT / "data"

REPORT_HEADING_PREFIX = "# LazyAlpha experiment — "
SECTION_RE = re.compile(r"^## ([^\r\n]+)\r?$", re.MULTILINE)
BOLD_LINE_RE = re.compile(r"^[ \t]*\*\*(.+?)\*\*", re.MULTILINE)
GENERATED_RE = re.compile(r"^Generated:[ \t]*(\S+)[ \t]*\r?$", re.MULTILINE)
PARAMS_RE = re.compile(r"^- Parameters:[ \t]?(.*?)(?:\r?$)", re.MULTILINE)

CATEGORY_ORDER = ("pass", "fail", "inconclusive", "informational", "not_evaluable")


class BuildError(RuntimeError):
    """A source-data or site-scaffolding error that must stop the build."""


@dataclass
class Section:
    heading: str
    body: str
    classification: str


@dataclass
class RegistryEntry:
    line_number: int
    raw: dict[str, Any]


@dataclass
class Report:
    source_path: Path
    filename: str
    family: str
    generated_at: datetime
    generated_at_source: str
    sections: list[Section]
    params_line: str
    verdict_text: str
    verdict_category: str
    verdict_label: str
    badge_class: str
    registry_matches: list[dict[str, Any]]
    registered: bool
    slug: str = ""
    variant_index: int = 0
    chart_filename: str | None = None


@dataclass
class ResearchNote:
    source_path: Path
    filename: str
    title: str
    generated_at_source: str | None
    body: str
    slug: str


def read_source_text(path: Path) -> str:
    """Decode UTF-8 without universal-newline conversion."""
    try:
        return path.read_bytes().decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise BuildError(f"{path.name}: report is not valid UTF-8: {exc}") from exc


def normalized_windows_path(value: str | Path) -> str:
    return ntpath.normcase(ntpath.normpath(str(value).replace("/", "\\")))


def slugify(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()


def classify_section(heading: str) -> str:
    if heading == "Experiment":
        return "experiment"
    if heading == "Data provenance":
        return "provenance"
    if heading.startswith("Research rationale"):
        return "rationale"
    if heading.startswith(("Net backtest metrics", "Available comparator metrics")):
        return "metrics"
    if heading.startswith("Walk-forward"):
        return "walkforward"
    if heading.startswith("Giudizio"):
        return "verdict"
    if heading.startswith("Ecosystem review"):
        return "ecosystem"
    return "extra"


def parse_iso8601(value: str, filename: str, field: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise BuildError(f"{filename}: invalid {field} ISO-8601 timestamp {value!r}") from exc


def bold_statements(body: str) -> list[str]:
    return [match.group(1) for match in BOLD_LINE_RE.finditer(body)]


def canonical_verdict(sections: list[Section], filename: str) -> tuple[str, str, str]:
    all_bold = [statement for section in sections for statement in bold_statements(section.body)]
    verdict_bold = [
        statement
        for section in sections
        if section.classification == "verdict"
        for statement in bold_statements(section.body)
    ]

    verdict_text: str | None = None
    for marker in ("Final validation judgment:", "Walk-forward verdict:"):
        verdict_text = next((text for text in all_bold if marker in text), None)
        if verdict_text is not None:
            break
    if verdict_text is None and verdict_bold:
        verdict_text = verdict_bold[0]
    if verdict_text is None:
        raise BuildError(f"{filename}: no canonical bold verdict statement found")

    if "NOT EVALUABLE" in verdict_text:
        category, label = "not_evaluable", "NOT EVALUABLE"
    elif "NOT RUN" in verdict_text:
        category, label = "not_evaluable", "NOT RUN"
    elif "INFORMATIONAL ONLY" in verdict_text:
        category, label = "informational", "INFORMATIONAL ONLY"
    elif "NON-CONCLUSIVE" in verdict_text:
        category, label = "informational", "NON-CONCLUSIVE"
    elif "INCONCLUSIVE" in verdict_text:
        category, label = "inconclusive", "INCONCLUSIVE"
    elif "PASS" in verdict_text:
        category, label = "pass", "PASS"
    elif "FAIL" in verdict_text:
        category, label = "fail", "FAIL"
    else:
        raise BuildError(
            f"{filename}: unrecognized verdict vocabulary in canonical statement {verdict_text!r}"
        )

    badge_class = (
        "verdict-badge--pass"
        if category == "pass"
        else "verdict-badge--fail"
        if category == "fail"
        else "verdict-badge--warn"
    )
    return verdict_text, category, label


def load_registry() -> list[RegistryEntry]:
    try:
        text = read_source_text(REGISTRY_PATH)
    except OSError as exc:
        raise BuildError(f"cannot read registry {REGISTRY_PATH}: {exc}") from exc

    entries: list[RegistryEntry] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            raise BuildError(f"{REGISTRY_PATH.name}: blank line at registry line {line_number}")
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as exc:
            raise BuildError(
                f"{REGISTRY_PATH.name}: invalid JSON at line {line_number}: {exc}"
            ) from exc
        if not isinstance(raw, dict):
            raise BuildError(f"{REGISTRY_PATH.name}: line {line_number} is not a JSON object")
        missing = {"timestamp", "strategy_name", "params", "report_path", "walk_forward_passed"} - raw.keys()
        if missing:
            raise BuildError(
                f"{REGISTRY_PATH.name}: line {line_number} missing fields: {', '.join(sorted(missing))}"
            )
        if not isinstance(raw["params"], dict):
            raise BuildError(f"{REGISTRY_PATH.name}: line {line_number} params is not an object")
        if not isinstance(raw["walk_forward_passed"], bool):
            raise BuildError(
                f"{REGISTRY_PATH.name}: line {line_number} walk_forward_passed is not boolean"
            )
        parse_iso8601(str(raw["timestamp"]), REGISTRY_PATH.name, f"line {line_number} timestamp")
        entries.append(RegistryEntry(line_number=line_number, raw=raw))
    return entries


def split_sections(text: str) -> list[Section]:
    matches = list(SECTION_RE.finditer(text))
    sections: list[Section] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        heading = match.group(1)
        sections.append(
            Section(
                heading=heading,
                body=text[match.end() : end],
                classification=classify_section(heading),
            )
        )
    return sections


def parse_report(path: Path, registry: list[RegistryEntry]) -> Report:
    text = read_source_text(path)
    first_nonblank = next((line.rstrip("\r") for line in text.splitlines() if line.strip()), "")
    if not first_nonblank.startswith(REPORT_HEADING_PREFIX):
        raise BuildError(
            f"{path.name}: first non-blank line must start with {REPORT_HEADING_PREFIX!r}; "
            f"found {first_nonblank!r}"
        )
    family = first_nonblank[len(REPORT_HEADING_PREFIX) :]
    if not family:
        raise BuildError(f"{path.name}: empty family name in report heading")

    first_lines = text.splitlines()[:5]
    generated_source: str | None = None
    for line in first_lines:
        match = re.fullmatch(r"Generated:[ \t]*(\S+)[ \t]*", line)
        if match:
            generated_source = match.group(1)
            break
    if generated_source is None:
        raise BuildError(f"{path.name}: missing Generated: ISO-8601 line within first five lines")
    generated_at = parse_iso8601(generated_source, path.name, "Generated")

    sections = split_sections(text)
    experiment_sections = [s for s in sections if s.classification == "experiment"]
    if not experiment_sections:
        raise BuildError(f"{path.name}: missing required ## Experiment section")
    params_match = PARAMS_RE.search(experiment_sections[0].body)
    if params_match is None:
        raise BuildError(f"{path.name}: Experiment section has no '- Parameters:' bullet")
    params_line = params_match.group(1)

    verdict_text, verdict_category, verdict_label = canonical_verdict(sections, path.name)
    badge_class = (
        "verdict-badge--pass"
        if verdict_category == "pass"
        else "verdict-badge--fail"
        if verdict_category == "fail"
        else "verdict-badge--warn"
    )

    report_key = normalized_windows_path(path.resolve())
    registry_matches = [
        {
            "timestamp": entry.raw["timestamp"],
            "walk_forward_passed": entry.raw["walk_forward_passed"],
            "params": entry.raw["params"],
        }
        for entry in registry
        if normalized_windows_path(str(entry.raw["report_path"])) == report_key
    ]
    return Report(
        source_path=path,
        filename=path.name,
        family=family,
        generated_at=generated_at,
        generated_at_source=generated_source,
        sections=sections,
        params_line=params_line,
        verdict_text=verdict_text,
        verdict_category=verdict_category,
        verdict_label=verdict_label,
        badge_class=badge_class,
        registry_matches=registry_matches,
        registered=bool(registry_matches),
    )


def parse_research_note(path: Path, text: str) -> ResearchNote:
    lines = text.splitlines(keepends=True)
    title_index = next((index for index, line in enumerate(lines) if line.strip()), None)
    if title_index is None:
        raise BuildError(f"{path.name}: non-empty research note has no non-blank title line")

    title_line = lines[title_index].rstrip("\r\n")
    title = re.sub(r"^#+[ \t]*", "", title_line)
    slug = slugify(title)
    if not slug:
        raise BuildError(f"{path.name}: research-note title {title!r} produces an empty slug")

    generated_source: str | None = None
    for line in text.splitlines()[:5]:
        match = re.search(r"(?:Generated|Generato il):[ \t]*(\S+)", line)
        if match:
            generated_source = match.group(1)
            break

    return ResearchNote(
        source_path=path,
        filename=path.name,
        title=title,
        generated_at_source=generated_source,
        body="".join(lines[title_index + 1 :]),
        slug=slug,
    )


def load_reports(registry: list[RegistryEntry]) -> tuple[list[Report], list[ResearchNote]]:
    try:
        paths = sorted(REPORTS_DIR.glob("*.md"), key=lambda path: path.name.lower())
    except OSError as exc:
        raise BuildError(f"cannot list reports directory {REPORTS_DIR}: {exc}") from exc

    reports: list[Report] = []
    research_notes: list[ResearchNote] = []
    errors: list[str] = []
    for path in paths:
        if path.name == ".gitkeep":
            continue
        if path.stat().st_size == 0:
            print(f"WARNING: skipping 0-byte report: {path.name}", file=sys.stderr)
            continue
        try:
            text = read_source_text(path)
            first_nonblank = next(
                (line.rstrip("\r") for line in text.splitlines() if line.strip()), ""
            )
            if first_nonblank.startswith(REPORT_HEADING_PREFIX):
                reports.append(parse_report(path, registry))
            else:
                research_notes.append(parse_research_note(path, text))
        except BuildError as exc:
            errors.append(str(exc))
    if errors:
        joined = "\n  - ".join(errors)
        raise BuildError(f"report validation failed:\n  - {joined}")
    seen_note_slugs: dict[str, str] = {}
    for note in research_notes:
        if note.slug in seen_note_slugs:
            raise BuildError(
                f"research-note slug collision: {seen_note_slugs[note.slug]!r} and "
                f"{note.filename!r} both produce {note.slug!r}"
            )
        seen_note_slugs[note.slug] = note.filename

    dated_notes = sorted(
        (note for note in research_notes if note.generated_at_source is not None),
        key=lambda note: (note.generated_at_source, note.filename.casefold()),
        reverse=True,
    )
    undated_notes = sorted(
        (note for note in research_notes if note.generated_at_source is None),
        key=lambda note: note.filename.casefold(),
    )
    return reports, dated_notes + undated_notes


def group_and_deduplicate(reports: list[Report]) -> tuple[dict[str, list[Report]], int]:
    grouped_raw: dict[str, list[Report]] = defaultdict(list)
    for report in reports:
        grouped_raw[report.family].append(report)

    grouped: dict[str, list[Report]] = {}
    discarded = 0
    seen_slugs: dict[str, str] = {}
    for family in sorted(grouped_raw, key=str.casefold):
        slug = slugify(family)
        if not slug:
            raise BuildError(f"family {family!r} produces an empty slug")
        if slug in seen_slugs and seen_slugs[slug] != family:
            raise BuildError(
                f"slug collision: families {seen_slugs[slug]!r} and {family!r} both produce {slug!r}"
            )
        seen_slugs[slug] = family

        by_params: dict[str, Report] = {}
        for report in grouped_raw[family]:
            current = by_params.get(report.params_line)
            if current is None or report.generated_at > current.generated_at:
                by_params[report.params_line] = report
        variants = sorted(by_params.values(), key=lambda report: (report.generated_at, report.filename))
        discarded += len(grouped_raw[family]) - len(variants)
        for index, report in enumerate(variants, start=1):
            report.slug = slug
            report.variant_index = index
        grouped[family] = variants
    return grouped, discarded


def badge(css_class: str, label: str) -> str:
    return (
        f'<span class="verdict-badge {html.escape(css_class, quote=True)}">'
        f"{html.escape(label)}</span>"
    )


def shorten(value: str, limit: int) -> str:
    return value if len(value) <= limit else value[: limit - 1] + "…"


def code_html(value: str, limit: int, href: str | None = None) -> str:
    escaped_full = html.escape(value, quote=True).replace("|", "&#124;")
    escaped_short = html.escape(shorten(value, limit)).replace("|", "&#124;")
    code = f"<code>{escaped_short}</code>"
    if href is None:
        return f'<span title="{escaped_full}">{code}</span>'
    return f'<a href="{html.escape(href, quote=True)}" title="{escaped_full}">{code}</a>'


def registered_short(report: Report) -> str:
    if not report.registered:
        return "—"
    count = len(report.registry_matches)
    return "✓" if count == 1 else f"✓ ({count} entries)"


def registered_detail(report: Report) -> str:
    if not report.registered:
        return "—"
    prefix = registered_short(report)
    details = "; ".join(
        f"{match['timestamp']} (walk_forward_passed={match['walk_forward_passed']})"
        for match in report.registry_matches
    )
    return f"{prefix} — {details}"


def markdown_table_rows(body: str) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            current.append([cell.strip() for cell in stripped[1:-1].split("|")])
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return tables


def parse_number(value: str) -> float | None:
    cleaned = value.strip().replace("%", "").replace(",", "")
    try:
        return float(cleaned)
    except ValueError:
        return None


def chart_values(report: Report) -> tuple[float, float, float, float] | None:
    metrics = next((s for s in report.sections if s.classification == "metrics"), None)
    if metrics is None:
        return None
    for table in markdown_table_rows(metrics.body):
        if len(table) < 3 or len(table[0]) < 3:
            continue
        header = table[0]
        benchmark_index = next(
            (index for index, value in enumerate(header) if value.strip().casefold() == "benchmark"),
            len(header) - 1,
        )
        strategy_index = 1
        if benchmark_index == strategy_index:
            continue
        data_rows = [row for row in table[2:] if len(row) == len(header)]
        return_row = next(
            (row for row in data_rows if row[0].strip().casefold() == "cumulative return"),
            None,
        )
        if return_row is None:
            return_row = next(
                (row for row in data_rows if "cumulative return" in row[0].casefold()), None
            )
        sharpe_row = next((row for row in data_rows if "sharpe" in row[0].casefold()), None)
        if return_row is None or sharpe_row is None:
            continue
        values = (
            parse_number(return_row[strategy_index]),
            parse_number(return_row[benchmark_index]),
            parse_number(sharpe_row[strategy_index]),
            parse_number(sharpe_row[benchmark_index]),
        )
        if all(value is not None for value in values):
            return values  # type: ignore[return-value]
    return None


def render_chart_svg(values: tuple[float, float, float, float]) -> bytes:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    strategy_return, benchmark_return, strategy_sharpe, benchmark_sharpe = values
    text_color = "#172033"
    colors = ["#6958d8", "#98a1b4"]
    figure, axes = plt.subplots(1, 2, figsize=(8, 3.35))
    figure.patch.set_alpha(0)
    for axis, plotted, ylabel in (
        (axes[0], [strategy_return, benchmark_return], "Return (%)"),
        (axes[1], [strategy_sharpe, benchmark_sharpe], "Sharpe"),
    ):
        axis.patch.set_alpha(0)
        axis.bar(["Strategy", "Benchmark"], plotted, color=colors, width=0.62)
        axis.set_ylabel(ylabel, color=text_color)
        axis.tick_params(colors=text_color)
        axis.axhline(0, color=text_color, linewidth=0.7, alpha=0.5)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
        axis.spines["bottom"].set_color(text_color)
        axis.spines["left"].set_color(text_color)
    figure.tight_layout()
    output = io.BytesIO()
    figure.savefig(output, format="svg", transparent=True, metadata={"Date": None})
    plt.close(figure)
    return output.getvalue()


def render_model_page(family: str, variants: list[Report], newline: str) -> str:
    earliest = variants[0].generated_at.date().isoformat()
    latest = variants[-1].generated_at.date().isoformat()
    lines = [
        f"# Strategy: {family}",
        "",
        f"{len(variants)} variant(s) documented · earliest {earliest} · latest {latest}.",
        "",
        "| Variant | Generated | Registered | Verdict |",
        "|---|---|---:|---|",
    ]
    for report in variants:
        lines.append(
            "| "
            + " | ".join(
                [
                    code_html(report.params_line, 80, f"#variant-{report.variant_index}"),
                    html.escape(report.generated_at_source),
                    registered_short(report),
                    badge(report.badge_class, report.verdict_label),
                ]
            )
            + " |"
        )
    output = newline.join(lines) + newline
    for report in variants:
        variant_lines = [
            "",
            f"### Variant {report.variant_index} {{: #variant-{report.variant_index} }}",
            "",
            f"**Generated:** {report.generated_at_source}  ",
            f"**Source report:** `{report.filename}`  ",
            f"**Registered:** {registered_detail(report)}",
            "",
            badge(report.badge_class, report.verdict_label),
            "",
        ]
        if report.chart_filename:
            variant_lines.extend(
                [
                    f'<img src="../assets/charts/{report.chart_filename}" alt="{html.escape(family, quote=True)} variant {report.variant_index} return and Sharpe comparison">',
                    "",
                ]
            )
        output += newline.join(variant_lines)
        raw_sections = "".join(f"#### {section.heading}{section.body}" for section in report.sections)
        # Append source section bodies without normalizing any of their bytes.
        output += raw_sections
        if not output.endswith(("\n", "\r")):
            output += newline
    return output


def render_research_note(note: ResearchNote, newline: str) -> str:
    generated = note.generated_at_source or "date not available"
    header = newline.join(
        [
            f"# {note.title}",
            "",
            "*This is a comparative research note, not a single-strategy model card. It may compare multiple variants and does not carry a single PASS/FAIL verdict badge.*",
            "",
            f"**Generated:** {generated}",
            "",
        ]
    )
    return header + newline + note.body


def render_notes_index(research_notes: list[ResearchNote], newline: str) -> str:
    lines = [
        "# Research notes",
        "",
        "These comparative and exploratory write-ups do not fit the single-strategy model-card format.",
        "",
    ]
    for note in research_notes:
        title = note.title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
        generated = note.generated_at_source or "date not available"
        lines.append(f"- [{title}](notes/{note.slug}.md) — {generated}")
    return newline.join(lines) + newline


def render_leaderboard(grouped: dict[str, list[Report]], newline: str) -> str:
    variants = sorted(
        (report for reports in grouped.values() for report in reports),
        key=lambda report: (report.generated_at, report.family, report.variant_index),
        reverse=True,
    )
    lines = [
        "# Leaderboard",
        "",
        "This lists every documented experiment variant, passing and failing alike, sourced directly from the individual reports.",
        "",
        "| Strategy | Params | Generated | Registered | Verdict |",
        "|---|---|---|---:|---|",
    ]
    for report in variants:
        strategy = html.escape(report.family).replace("|", "&#124;")
        lines.append(
            f"| [{strategy}](models/{report.slug}.md#variant-{report.variant_index}) | "
            f"{code_html(report.params_line, 80)} | {html.escape(report.generated_at_source)} | "
            f"{registered_short(report)} | {badge(report.badge_class, report.verdict_label)} |"
        )
    return newline.join(lines) + newline


def registry_badge(entry: RegistryEntry) -> str:
    passed = entry.raw["walk_forward_passed"]
    return badge("verdict-badge--pass" if passed else "verdict-badge--fail", "PASS" if passed else "FAIL")


def render_changelog(
    registry: list[RegistryEntry], grouped: dict[str, list[Report]], newline: str
) -> str:
    slug_by_family = {family: variants[0].slug for family, variants in grouped.items()}
    lines = [
        "# Changelog",
        "",
        "This is LazyAlpha's own append-only experiment registry, in its original order, unedited.",
        "",
    ]
    for entry in registry:
        raw = entry.raw
        strategy_name = str(raw["strategy_name"])
        strategy_display = html.escape(strategy_name)
        if strategy_name in slug_by_family:
            strategy_display = f"[{strategy_display}](models/{slug_by_family[strategy_name]}.md)"
        compact_params = json.dumps(raw["params"], sort_keys=True, ensure_ascii=False)
        lines.append(
            f"- {html.escape(str(raw['timestamp']))} · {strategy_display} · "
            f"{code_html(compact_params, 120)} · {registry_badge(entry)}"
        )
    return newline.join(lines) + newline


def detect_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def updated_index(index_text: str, total: int, passes: int) -> str:
    newline = detect_newline(index_text)
    start_marker = "<!-- STATS:START -->"
    end_marker = "<!-- STATS:END -->"
    start = index_text.find(start_marker)
    end = index_text.find(end_marker)
    if start < 0 or end < 0 or end <= start:
        raise BuildError("docs/index.md: missing or misordered literal STATS markers")
    content_start = start + len(start_marker)
    content_end = end
    replacement = newline + newline.join(
        [
            '<div class="la-stat-row">',
            f'  <div class="la-stat"><span class="la-stat__value">{total}</span><span class="la-stat__label">Experiments documented</span></div>',
            f'  <div class="la-stat"><span class="la-stat__value">{passes}</span><span class="la-stat__label">Walk-forward PASS</span></div>',
            f'  <div class="la-stat"><span class="la-stat__value">{total - passes}</span><span class="la-stat__label">FAIL / inconclusive / blocked</span></div>',
            "</div>",
        ]
    ) + newline
    return index_text[:content_start] + replacement + index_text[content_end:]


def yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def updated_mkdocs(mkdocs_text: str, grouped: dict[str, list[Report]]) -> str:
    newline = detect_newline(mkdocs_text)
    lines = mkdocs_text.splitlines(keepends=True)
    nav_start = next((i for i, line in enumerate(lines) if line.rstrip("\r\n") == "nav:"), None)
    if nav_start is None:
        raise BuildError("mkdocs.yml: missing top-level nav: block")
    nav_end = nav_start + 1
    while nav_end < len(lines) and lines[nav_end].startswith((" ", "\t")):
        nav_end += 1

    nav_lines = [
        "nav:",
        "  - Home: index.md",
        "  - Methodology: methodology.md",
        "  - Leaderboard: leaderboard.md",
        "  - Changelog: changelog.md",
        "  - Notes: notes.md",
        "  - Models:",
    ]
    for family in sorted(grouped, key=str.casefold):
        slug = grouped[family][0].slug
        nav_lines.append(f"      - {yaml_single_quote(family)}: models/{slug}.md")
    nav_block = newline.join(nav_lines) + newline
    return "".join(lines[:nav_start]) + nav_block + "".join(lines[nav_end:])


def report_as_json(report: Report) -> dict[str, Any]:
    return {
        "source_path": str(report.source_path),
        "filename": report.filename,
        "family": report.family,
        "slug": report.slug,
        "variant_index": report.variant_index,
        "generated_at": report.generated_at.isoformat(),
        "generated_at_source": report.generated_at_source,
        "params_line": report.params_line,
        "verdict_text": report.verdict_text,
        "verdict_category": report.verdict_category,
        "verdict_label": report.verdict_label,
        "badge_class": report.badge_class,
        "registered": report.registered,
        "registry_matches": report.registry_matches,
        "chart_filename": report.chart_filename,
        "sections": [
            {
                "heading": section.heading,
                "classification": section.classification,
                "raw_markdown_body": section.body,
            }
            for section in report.sections
        ],
    }


def atomic_write_text(path: Path, content: str) -> None:
    temp = path.with_name(path.name + ".tmp")
    temp.write_bytes(content.encode("utf-8"))
    temp.replace(path)


def atomic_write_bytes(path: Path, content: bytes) -> None:
    temp = path.with_name(path.name + ".tmp")
    temp.write_bytes(content)
    temp.replace(path)


def build() -> None:
    # Read and validate every source and every edit target before creating outputs.
    registry = load_registry()
    reports, research_notes = load_reports(registry)
    grouped, duplicate_count = group_and_deduplicate(reports)
    variants = [report for family_reports in grouped.values() for report in family_reports]

    try:
        index_text = read_source_text(DOCS_DIR / "index.md")
        mkdocs_text = read_source_text(SITE_ROOT / "mkdocs.yml")
    except OSError as exc:
        raise BuildError(f"cannot read site scaffold: {exc}") from exc

    index_newline = detect_newline(index_text)
    mkdocs_newline = detect_newline(mkdocs_text)
    chart_outputs: dict[str, bytes] = {}
    for report in variants:
        values = chart_values(report)
        if values is not None:
            report.chart_filename = f"{report.slug}__variant-{report.variant_index}.svg"
            chart_outputs[report.chart_filename] = render_chart_svg(values)

    model_outputs = {
        f"{variants_for_family[0].slug}.md": render_model_page(
            family, variants_for_family, index_newline
        )
        for family, variants_for_family in grouped.items()
    }
    note_outputs = {
        f"{note.slug}.md": render_research_note(note, index_newline)
        for note in research_notes
    }
    notes_index = render_notes_index(research_notes, index_newline)
    leaderboard = render_leaderboard(grouped, index_newline)
    changelog = render_changelog(registry, grouped, index_newline)
    passes = sum(report.verdict_category == "pass" for report in variants)
    new_index = updated_index(index_text, len(variants), passes)
    new_mkdocs = updated_mkdocs(mkdocs_text, grouped)
    dataset = {
        "source_root": str(LAZYALPHA_ROOT),
        "registry_path": str(REGISTRY_PATH),
        "registry_entries": [entry.raw for entry in registry],
        "duplicate_reruns_discarded": duplicate_count,
        "families": {
            family: {
                "slug": family_variants[0].slug,
                "variants": [report_as_json(report) for report in family_variants],
            }
            for family, family_variants in grouped.items()
        },
    }
    dataset_json = json.dumps(dataset, indent=2, ensure_ascii=False) + "\n"

    # All parsing, validation, rendering, and chart construction succeeded; writes begin here.
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in model_outputs.items():
        atomic_write_text(MODELS_DIR / filename, content)
    for filename, content in chart_outputs.items():
        atomic_write_bytes(CHARTS_DIR / filename, content)
    for filename, content in note_outputs.items():
        atomic_write_text(NOTES_DIR / filename, content)
    atomic_write_text(DOCS_DIR / "notes.md", notes_index)
    atomic_write_text(DOCS_DIR / "leaderboard.md", leaderboard)
    atomic_write_text(DOCS_DIR / "changelog.md", changelog)
    atomic_write_text(DOCS_DIR / "index.md", new_index)
    atomic_write_text(SITE_ROOT / "mkdocs.yml", new_mkdocs)
    atomic_write_text(DATA_DIR / "experiments.generated.json", dataset_json)

    categories = Counter(report.verdict_category for report in variants)
    registered = sum(report.registered for report in variants)
    breakdown = ", ".join(f"{category}={categories[category]}" for category in CATEGORY_ORDER)
    print(f"Families: {len(grouped)}")
    print(f"Variants: {len(variants)}")
    print(f"Research notes: {len(research_notes)}")
    print(f"Duplicate reruns discarded: {duplicate_count}")
    print(f"Registered variants: {registered}")
    print(f"Unregistered variants: {len(variants) - registered}")
    print(f"Verdicts: {breakdown}")


def main() -> int:
    try:
        build()
    except (BuildError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
