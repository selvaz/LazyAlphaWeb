# LazyAlphaWeb plan proposal (2026-09-11)

## What this site is for

LazyAlpha is "a budget-aware research and development agent for systematic
trading strategies" whose own README states plainly: "It is research
infrastructure, not an execution system or investment advice." This site's
only job is to make that research legible to a human reader: for every
strategy family LazyAlpha has actually built and tested, show real context
(why this family, what gap it fills), the real cited sources LazyAlpha's own
research used, and the full, honest backtest results — full-sample metrics,
walk-forward development/out-of-sample breakdown, the explicit verdict, and
the benchmark comparison — exactly as LazyAlpha's own reports already state
them.

**Honest-reporting rule (binding, carried into every later cycle):** the site
must never spin a loss into a win or bury a FAIL. If a report says
`FAIL: degrades out of sample`, `INCONCLUSIVE`, `INFORMATIONAL ONLY /
NON-CONCLUSIVE`, or `NOT EVALUABLE` / `NOT RUN`, the site states that verdict
in those terms, as prominently as a PASS. Every number, quote, source link and
verdict string published on the site must be traceable verbatim to a literal
string already present in a LazyAlpha `reports/*.md` file or
`lazyalpha/state/experiments.jsonl` record. The generator must never compute,
estimate, or invent a metric, a source, or a verdict that is not already
written down in LazyAlpha's own material. If a report cannot be parsed
confidently, the build must fail loudly rather than silently publish a
guess.

## Current LazyAlpha state (read 2026-09-11, will change daily)

- `lazyalpha/state/experiments.jsonl`: 2 registered experiments —
  `ma_crossover_50_200` (walk-forward **PASS**) and
  `regime_conditional_ma_50_200_state_0` (walk-forward **FAIL**).
- `reports/`: 28 files. Beyond the two registered strategies above, there are
  distinct, fully-written-up experiments that are **not** in the registry
  because they were never a clean pass/fail candidate:
  - `sentiment_conditional_ma_50_200_3d.md` — digest-sentiment gate, verdict
    **INFORMATIONAL ONLY / NON-CONCLUSIVE** (history too short for a
    dev/OOS split; explicitly a smoke test, not a strategy verdict).
  - `policy_conditional_ma_spy_qqq.md` — point-in-time monetary-policy gate,
    verdict **NOT EVALUABLE** (`NOT RUN`: required point-in-time macro
    coverage is incomplete; the report explains exactly why and refuses to
    fabricate an information set the database doesn't contain).
  - `example_ma_crossover_spy_qqq.md` — the committed v0.1 reference report
    (full-sample only, no walk-forward section, superseded by the v0.2
    timestamped rerun but kept as the reviewed original).
  - ~21 timestamped `ma_crossover_5_20.md` files — repeated dev-loop runs of
    the same untested fast/slow pair, never registered. These are iteration
    noise, not 21 separate models; the site must collapse them to the single
    latest one, not list 21 near-duplicate cards.
- `docs/candidate-strategy-families.md`: 4 documented, evidence-cited
  candidate families (regime-conditional switching, point-in-time macro
  conditioning, CFTC positioning, LazyCrawler sentiment) plus a "daily
  tournament" framework idea for later. Two of the four already have a real
  experiment report (regime, sentiment); two do not yet (CFTC, and the macro
  family is blocked pending point-in-time coverage per the policy report).
- LazyAlpha's own `PLAN_PROPOSAL.md` next-steps order: harden the protocol
  (online research, parameter-search rigor, cost realism) before adding more
  candidate families. The site must reflect whatever actually exists on a
  given day, not a roadmap — it documents completed work, not intentions.

This confirms the site cannot be a one-time hand-written page: LazyAlpha adds
and revises experiments daily (2 registry entries and several new reports
appeared within the last 24 hours alone), so the site needs a repeatable,
re-runnable build, not hand-edited HTML/Markdown.

## Technology choice: MkDocs + Material, decided independently

This ecosystem already runs one public doc site this way
(`lazybridgewebsite`), proven for GitHub Pages + Actions deploy. I considered
it rather than copying it blindly:

- **Why MkDocs Material fits here too:** the actual content unit is a
  structured Markdown report with tables (metrics, walk-forward windows),
  admonitions (verdicts, known risks), and links (sources) — exactly what
  Material renders natively and well (sortable/striped tables, colored
  admonition blocks, dark/light mode, built-in search across model cards,
  code-copy for parameter blocks). A generator that emits Markdown is far
  less code and far fewer failure modes than emitting HTML/JSX, which matters
  because this pipeline runs unattended, daily, driven by an agent, not a
  human reviewing a diff carefully every time.
- **Why not a heavier custom stack (e.g. Astro/Next + React charts):** more
  flexible for bespoke interactive visuals, but the interactive-chart value
  is low here — the honest thing to chart is exactly the numbers already in
  the report tables, not a synthetic recomputation from raw prices (LazyAlpha
  itself doesn't publish daily equity-curve series, only summary metrics per
  window). A heavier JS build also adds real daily-pipeline fragility for a
  single-maintainer, agent-run site. Verdict: not worth it for the "figa" bar
  here.
- **How this site avoids looking like a generic docs site (the "molto figa"
  bar) without adding fragile custom tooling:**
  - a real landing page (`index.md`) with a hero, a one-line mission
    statement quoting LazyAlpha's own "research infrastructure, not a track
    record" framing, and live-generated headline stats (N experiments, N
    PASS / N FAIL / N inconclusive-or-blocked) instead of a bare doc index;
  - one **model card** per strategy family, not a wall of tables: context
    and references first, then a compact full-sample metrics table, then the
    walk-forward dev/OOS table, then a clearly color-coded verdict
    admonition (green PASS / red FAIL / gray inconclusive-or-blocked), then
    known risks and ecosystem-review notes — matching the order a person
    actually wants to read it in, not the order the raw report happens to
    use;
  - one static comparison chart per model (matplotlib, generated at build
    time straight from the already-reported strategy/benchmark numbers —
    return and Sharpe bars side by side), rendered as a checked-in SVG/PNG,
    zero client-side JS, zero recomputation risk;
  - a **leaderboard/comparison page** listing every model with its verdict
    badge, so the honest wins/losses record is visible in one place, not
    just buried inside individual cards;
  - a **methodology page** that explains, once, in plain language, what a
    PASS/FAIL walk-forward verdict means here, what INCONCLUSIVE /
    INFORMATIONAL ONLY / NOT EVALUABLE mean, the cost/lag/window
    conventions, and repeats the honest-reporting rule so a reader never
    mistakes a passing backtest for a live track record.

## Site structure

```
docs/
  index.md                 hand-maintained hero + live-generated headline stats block
  methodology.md           hand-maintained: verdict vocabulary, conventions, honest-reporting rule
  models/
    ma-crossover-50-200.md         generated
    regime-conditional-ma.md       generated
    sentiment-conditional-ma.md    generated
    policy-conditional-ma.md       generated (labeled NOT EVALUABLE / blocked)
    ...                            one file per distinct strategy identity, latest report wins
  leaderboard.md            generated: every model, verdict badge, key metrics, sorted by date
  changelog.md              generated: chronological feed straight from experiments.jsonl
  assets/charts/*.svg       generated: one comparison chart per model
data/
  experiments.generated.json   generated intermediate artifact (for debugging/verification, checked in)
scripts/
  build_site.py             the generator (stdlib + matplotlib only)
tests/
  test_build.py              spot-checks generated pages against source report strings
mkdocs.yml
requirements.txt
.github/workflows/deploy.yml
```

## The generator (`scripts/build_site.py`)

1. Read-only against LazyAlpha: `reports/*.md`,
   `lazyalpha/state/experiments.jsonl`, `docs/candidate-strategy-families.md`,
   `README.md`. Never writes there.
2. Group `reports/*.md` by strategy identity (parsed from the report's H1,
   `# LazyAlpha experiment — <name>`, stripped of any per-run seed/window
   suffix that isn't a real parameter difference); within each group keep
   only the chronologically latest report (by the `Generated:` timestamp),
   so the ~21 duplicate `ma_crossover_5_20` dev-loop runs collapse to one
   card instead of 21.
3. For each surviving report, parse structurally: title/params, data
   provenance, research rationale + source links, known risks, the metrics
   table(s), the walk-forward table (if present), the literal verdict
   sentence(s), and the ecosystem-review bullets. Cross-reference
   `experiments.jsonl` only to annotate whether the strategy is registered
   and to source the canonical `walk_forward_passed` flag and timestamp —
   never to filter out an honest non-registered write-up like the blocked
   policy report or the informational sentiment report, since hiding those
   would misrepresent the record.
4. Emit one Markdown model card per surviving group into `docs/models/`, one
   row per group into `docs/leaderboard.md`, one chronological entry per
   registry line into `docs/changelog.md`, one chart per group into
   `docs/assets/charts/`, and the full parsed dataset into
   `data/experiments.generated.json`.
5. Regenerate `index.md`'s live-stats block (count of models, PASS/FAIL/other
   split) via a marked region (`<!-- STATS:START -->` / `<!-- STATS:END -->`)
   so the rest of the hand-written hero copy survives untouched across runs.
6. Fail loudly (non-zero exit, no partial publish) if any report cannot be
   parsed with confidence, rather than guessing at a missing field.

## Verification (`tests/test_build.py`)

For every generated model card, assert each published numeric metric string
and each published verdict string is a verbatim substring of its source
`reports/*.md` file. This is a mechanical, cheap guardrail against the
generator ever paraphrasing a number wrong or softening a verdict — on top
of my own manual spot-check against the source report each time I verify a
delegated build, as required by my working instructions.

## GitHub Pages / Actions — what needs the CEO, explicitly

Two one-time, structural steps are **not mine to do unannounced** and are
called out here for CEO action/approval before anything is public:

1. **Create the `LazyAlphaWeb` GitHub repository and make it public.** I do
   not have the standing to create or flip visibility on a GitHub repo
   myself; this needs the CEO (or operator, via the CEO) to do it once.
2. **First-time GitHub Pages + Actions configuration** on that repo (Pages
   source = GitHub Actions; confirm default branch name; confirm whether a
   custom domain/CNAME is wanted now or later — `lazybridgewebsite` has one,
   LazyAlphaWeb doesn't need one to go live, so I propose shipping first on
   the default `<owner>.github.io/LazyAlphaWeb/` URL and revisiting a custom
   domain as a separate, later decision).

Once both exist, the repeatable loop (regenerate from LazyAlpha's current
state, commit, push to LazyAlphaWeb's own remote) is pre-authorized by the
operator to run autonomously on my normal daily cycle — no per-day approval
needed for that push itself. Every `codex_write`/`claude_write` call I make to
do the actual generation work still requires its own CEO approval ticket
regardless (structural gate, not something either of us can waive) — that is
separate from, and does not reintroduce, a daily "may I publish" question.

## Proposed steps (this is what I will ask `set_plan` to track next)

1. Escalate to the CEO: request creation of the public `LazyAlphaWeb` GitHub
   repository and first-time Pages/Actions configuration, per the section
   above. Block on this before any push (local scaffolding/build work can
   proceed in parallel without a remote).
2. Scaffold the repo: `mkdocs.yml` (Material theme, LazyAlpha-specific
   branding distinct from LazyBridge's), `requirements.txt`, hand-written
   `docs/index.md` hero and `docs/methodology.md` (verdict vocabulary,
   conventions, the honest-reporting rule verbatim), `.gitignore`.
3. Build `scripts/build_site.py` per the generator spec above, run it once
   locally against LazyAlpha's current state, and hand-verify a sample of
   generated pages against their source report files line by line.
4. Add `tests/test_build.py` verbatim-substring verification and wire it to
   run before every publish.
5. Add `.github/workflows/deploy.yml`: on push to the default branch,
   install requirements and run `mkdocs build --strict` then deploy (mkdocs
   `gh-deploy`, matching the proven `lazybridgewebsite` pattern) to GitHub
   Pages.
6. First real commit + push (after step 1 is confirmed done), confirm the
   live Pages URL renders correctly, and escalate that milestone to the CEO
   for operator visibility.
7. Establish the standing daily-maintenance step in the plan: each cycle,
   re-run the generator against LazyAlpha's current state, diff the output,
   hand-verify anything new (a new registry entry, a new report, a changed
   verdict) against its source file, commit, and push. Escalate instead of
   guessing on any genuine judgment call (new strategy family presentation,
   ambiguous verdict wording, structural site/design changes) rather than
   resolving it unilaterally.
