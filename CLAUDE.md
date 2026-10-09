# CLAUDE.md : Dog Training Guide

Nick Stoltz's reader-facing dog training guidebook. **Readers of `guide/` are dog owners with no technical background.** Readers of `evidence/` and `maintainers/` are AI agents and Nick. Keep the two audiences separate in every edit.

**Folder:** `C:\Users\Stoltz\Desktop\Claude Projects\Dog Training` (created 2026-10-08). Shared externally via Google Drive or GitHub, so every file in `guide/` must stand alone without this file.

---

## Session protocol

**Start:** read this file, then `maintainers/HANDOFF.md`. Open a third file only when the task needs it.

**During:** every new claim written into `guide/` gets a row in `evidence/claims.md` the same edit, with a source row in `evidence/sources.md`. No row, no claim.

**End:** overwrite `maintainers/HANDOFF.md` (under 30 lines, with a Retro); refresh `maintainers/TASKS.md`; if a grade, verdict, or legal fact was reversed, add a `maintainers/CHANGELOG.md` entry.

---

## Writing protocol

Two protocols, by folder. Both in `maintainers/writing-protocol.md`. Summary:

| Folder | Audience | Rules |
|---|---|---|
| `guide/` | Dog owners | Plain words, short paragraphs, fixed page template, under 80 lines, no inline citations, evidence label in words, claim IDs only in the footer line. Define any term on first use or link to `glossary.md`. |
| `evidence/`, `maintainers/` | Agents and Nick | Tables, one row per item, IDs, dates on every verdict, no narrative. |

Everywhere: no em dashes, no emojis, absolute dates (YYYY-MM-DD), a verdict per item with a short reason.

**Line budgets:** `CLAUDE.md` 150; `HANDOFF.md` 30; any `guide/` page 80; `evidence/claims.md` and `sources.md` 200 each, then split by topic; `research/` frozen.

---

## Where everything lives

| Path | Holds | Add here when | Edit trigger |
|---|---|---|---|
| `README.md` | Reader hub: routing table, folder map, evidence legend. | A new reader entry point | When structure changes |
| `AGENTS.md` | Pointer to this file. | Never | Rarely |
| `guide/01-start-here/` | Orientation: how to use, the basics, body language, equipment, when to get help, glossary. | A concept every reader needs before any problem page | When a basic changes |
| `guide/02-methods/` | One page per training philosophy plus the comparison overview. | A method is added | When evidence changes a verdict |
| `guide/03-problems/` | One page per behavior problem. Opens with `first-rule-see-the-vet.md`. | A new problem | When a protocol or grade changes |
| `guide/04-protocols/` | Step-by-step cards referenced by problem pages. One technique per file. | A problem page needs steps longer than 10 lines | When steps change |
| `guide/05-development/` | Life stages: puppy, adolescent, adopted adult, senior; breed and genetics. | A stage-specific fact | When evidence changes |
| `guide/06-tools/` | Worksheets and templates for readers: household plan, training log, measurement sheet, comparison worksheet, medication conversation guide. | A reader needs a fill-in tool | When a tool changes |
| `guide/_templates/` | Page templates for method, problem, protocol pages. | The page shape changes | Rarely |
| `evidence/claims.md` | One row per claim: ID, claim, grade, source IDs, guide pages using it, verified date. | Any claim enters `guide/` | Same edit |
| `evidence/sources.md` | One row per source: ID, citation, link, type, verified Y/N, date. | A new source is cited | Same edit |
| `evidence/comparison-matrix.md` | Method matrix and problem matrix, current answer only. | A cell changes | When a grade or verdict changes |
| `evidence/legal-status.md` | E-collar and tool legality by jurisdiction, confidence, last-verified date. | A jurisdiction is added or changes | On verification |
| `evidence/open-questions.md` | Unverified assumptions the guide currently relies on. | A guide page rests on something unverified | Every session end |
| `maintainers/HANDOFF.md`, `TASKS.md`, `CHANGELOG.md` | Launch state; verification and build queue; reversals. | Per session protocol | Per session protocol |
| `maintainers/*.md` (procedures) | Evidence grading, page build, verification, comparison method, writing protocol. | A procedure is learned | When a procedure changes |
| `research/` | Dated research reports, frozen. First: `2026-10-08-comparative-reference-report.md`. | A full research write-up | Add only; status banner may point at CHANGELOG |
| `archive/` | Retired files and past handoffs. | A file's job is finished | Append only |

---

## Lifecycle

| Trigger | Action |
|---|---|
| New problem or method page | Copy the template from `guide/_templates/`, fill every section, add claim rows, add the page to the `README.md` routing table if it is an entry point. |
| A claim's evidence grade changes | Update `claims.md`, update the label on every guide page listed in that row, add a `CHANGELOG.md` entry. |
| A source is verified | Flip `sources.md` Verified to Y with date; remove the item from `TASKS.md`. |
| A legal fact changes | Update `legal-status.md` row and date, then every guide page that states it (`balanced-training.md`, `equipment.md`). |
| A reader tool is used in a real case | Record what broke in `maintainers/HANDOFF.md` Retro; fix the tool the same session. |

---

## Locked decisions

| Decision | Value | Decided |
|---|---|---|
| Default recommendation | Reward-based training under LIMA / Humane Hierarchy. Aversive methods are described and compared, never recommended. | 2026-10-08 |
| Scope | Not tied to one dog. Pet dogs, all ages. Training methods plus behavior modification. Sports and service work out of scope. | 2026-10-08 |
| Medication | Described as a veterinary adjunct with evidence grades. Never dosed. Always "talk to your vet". | 2026-10-08 |
| Audience split | `guide/` for owners, `evidence/` and `maintainers/` for agents. No cross-contamination. | 2026-10-08 |
| Protocol numbers | Step cards give starting numbers labeled "starting point, adjust to your dog", graded Consensus unless a study supports them. | 2026-10-08 |

---

## Guardrails for any AI session

1. **Never invent a study, statistic, or legal fact.** If it is not in `evidence/sources.md`, search and verify first, or leave it out.
2. **Never write medication doses.** Drug names, evidence, and "ask your vet" only.
3. **Readers are not agents.** Never put IDs, tables of sources, or procedure language inside a `guide/` page beyond the one-line evidence footer.
4. **Say when earlier content was wrong, immediately,** fix the page, and log it in `CHANGELOG.md`.
5. **Verdict per item** (apply / check first / hold / skip) with a short reason. Document updates are done and reported in a line, never offered.
6. **At most one clarifying question per turn,** and only when the answer changes the action.
7. **Safety first on aggression pages.** Any content touching bites, children, or muzzles leads with safety and referral, never with a training trick.

## Rules learned here

1. **Legal claims are date-stamped and confidence-rated.** (2026-10-08: the "England banned e-collars in 2024" belief was wrong; the regulations never came into force.)
