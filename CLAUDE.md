# LLM Wiki Schema — MLCC Research

> **Role & methodology live elsewhere — read these first:**
> - [AGENTS.md](./AGENTS.md) — agent role: 20-year MLCC engineer. Mission, research pillars.
> - [RESEARCH_PLAN.md](./RESEARCH_PLAN.md) — what to research, where to look, how to record findings, sequencing.
>
> This file is the **wiki schema**: it tells the wiki-maintainer skill how to structure pages in `wiki/`. It does NOT redefine the project mission.

## Domain

A persistent, interlinked knowledge base for **Multi-Layer Ceramic Capacitor (MLCC)** engineering. Topics span four pillars (see RESEARCH_PLAN.md §1–4):

1. Manufacturing process
2. Market & product lineups
3. Academic publications & patents
4. Design rules & specs

The wiki's long-term deliverable is a **design-rule synthesis** keyed to real datasheet behavior.

## Directory layout

```
resources/        # raw, immutable source material (was "sources/" in the skill default)
  assets/         # images, PDFs, datasheet snapshots
  manufacturing/  # raw notes & dumps about process
  market/         # datasheets, catalogs, lineup CSVs
  literature/     # paper PDFs / patent text
  design-rules/   # standards excerpts, app notes
wiki/             # synthesized, interlinked notes (Obsidian-compatible)
  entities/       # companies, product series, materials, standards bodies
  concepts/       # process steps, dielectric classes, failure modes, design rules
  sources/        # one summary page per ingested document
  comparisons/    # cross-vendor or cross-class comparison tables
  queries/        # filed answers to /wiki query
  index.md
  log.md
  overview.md
```

`.wiki-config.json` maps the skill's `sources_dir` → `resources` and `wiki_dir` → `wiki`.

## Source types

| Tier | Type | Where it lands | Wiki page goes in |
|---|---|---|---|
| T1 | Manufacturer datasheet / catalog | `resources/market/` (PDF in `resources/assets/` if downloaded) | `wiki/sources/` |
| T2 | Standards (EIA, IEC, AEC-Q200, JIS) | `resources/design-rules/` | `wiki/sources/` and concept pages under `wiki/concepts/` |
| T3 | Peer-reviewed paper | `resources/literature/` | `wiki/sources/` |
| T4 | Granted patent | `resources/literature/` | `wiki/sources/` |
| T5 | Industry whitepaper / market report | `resources/market/` | `wiki/sources/` |
| T6 | Vendor app note / blog | `resources/<topic>/` | summary into existing pages; standalone wiki/source page only if novel |

Always record source revision/date in the page's `sources:` frontmatter.

## Page types

### Entities (`wiki/entities/`)
Distinct named things. **Every entity page carries exactly one classification tag** from the vocabulary below.

**Entity classification vocabulary:**
- `company` — Murata, SEMCO, TDK, Taiyo Yuden, Yageo, KEMET, Walsin, KYOCERA AVX, Vishay, Fenghua, …
- `series` — product series (Murata GRM/GCM/GJM, SEMCO CL, TDK C-series, …)
- `material` — BaTiO₃, doped variants, Ni paste, Cu termination, …
- `standard` — EIA RS-198, IEC 60384-1/-21/-22, AEC-Q200, JIS C 5101, JEDEC docs
- `person` — researchers, inventors named on key patents/papers
- `org` — non-company organizations (EIA, IEC, JEDEC, universities, consortia)

### Concepts (`wiki/concepts/`)
Process steps (tape-casting, sintering, BME firing), dielectric classes (X7R, C0G), characteristics (TCC, DC-bias derating, ESR, ESL, aging), failure modes (flex crack, delamination, IR degradation), design rules.

### Source summaries (`wiki/sources/`)
One page per ingested document. Captures key claims, parameter ranges, figures of merit, and unresolved questions.

### Comparisons (`wiki/comparisons/`)
Cross-vendor or cross-class side-by-sides. Example: "0402 X7R 1 µF 6.3 V across Murata/SEMCO/TDK/TY", "C0G vs X7R for resonant-circuit timing caps".

### Queries (`wiki/queries/`)
Filed answers to `/wiki query` questions.

## Conventions

- YAML frontmatter on every page (schema below).
- Obsidian-style `[[wikilinks]]`; kebab-case filenames.
- Dates: `YYYY-MM-DD`.
- Units: SI; keep datasheet's original-unit value in parens if it differs.
- Contradictions: `> [!warning] Contradiction` callout — never silently overwrite.
- Tag policy from SKILL.md applies: max 3 tags, kebab-case, no tag that names a page-worthy concept.
- **Citations**: every numerical claim must be traceable to a source listed in `resources/bibliography.md`. Use short keys like `[murata-grm-2024]`, `[us10937593]`, `[moulson-herbert-2003]`.

## Frontmatter schema

```yaml
title: string               # required
type: entity | concept | source | comparison | query    # required
created: YYYY-MM-DD         # required
updated: YYYY-MM-DD         # required
sources: [filename.md, ...] # required (except index/log/overview)
tags: [kebab-case, ...]     # ≤ 3; entity pages MUST include exactly one of {company,series,material,standard,person,org}
```

## Maintenance

This schema co-evolves with the corpus. Update when new entity types, new dielectric codes, or new source tiers appear. Don't redefine project mission here — that's in `AGENTS.md` / `RESEARCH_PLAN.md`.
