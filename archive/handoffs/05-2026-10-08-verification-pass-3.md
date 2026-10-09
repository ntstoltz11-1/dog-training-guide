# Handoff 05 : Verification pass 3 done, priority 1 and 2 cleared, one grade change

**Date:** 2026-10-08.

## Where things stand

- **47 of 61 sources verified.** Session 05 cleared the two full-text follow-ups (S-03, S-18) and all priority-2 studies, statements, certifying bodies, and two European statutes. New sources S-56 to S-61.
- **Eight corrections** in [`CHANGELOG.md`](CHANGELOG.md). Two claims lost numbers that could not be traced to the primary text: Herron's "0 to 6%" for reward methods (only in an image; now "very few") and the dexmedetomidine "odds ratio 3.4" (now 72% vs 37%). C-08 "faster" became "fewer sessions"; daily training wins on the calendar, weekly wins per session.
- **One grade change:** imepitoin (C-18) Moderate to Strong. The stored S-22 title was a different paper; the real trial is Engel 2019, JVIM, 238 dogs, with 48% adverse events and an FDA aggression note. "EU approved" was replaced with the confirmed FDA approval (2018-12).
- **Legal:** Germany and Austria raised to High on statute plus court records. Netherlands, Switzerland, Scandinavia still Moderate.
- **Guide pages edited:** 01/basics, 01/when-to-get-help (credential table now carries each body's actual requirements), 02/dominance, 02/overview, 03/fear, 06/medication. All under 80 lines.
- **Session 04 (same day):** formatting pass; link text is now page titles via `titleize.py`, run after `linkify.py` whenever pages are added.

## Next session

1. Legal: Netherlands, Switzerland, Denmark, Sweden, Norway, Finland statutes ([`TASKS.md`](TASKS.md) Verify, priority 2). Confirm imepitoin EU authorisation.
2. Priority 3 rows: Scotland vote source, C-BARQ, the four pre-visit medication trials, S-27 journal and year.
3. Nick test-reads [`decision-tree.md`](../guide/01-start-here/decision-tree.md) and [`children-and-dogs.md`](../guide/03-problems/children-and-dogs.md) cold.
4. Consider body-language diagrams ([`TASKS.md`](TASKS.md) Build).

## Retro (session 05)

- Went wrong: three DOIs were nearly written into sources.md from memory before a search showed they could not be confirmed; they were replaced with the verified journal links. The no-invent rule has to apply to identifiers, not just findings.
- Went right: fetching the Herron PDF settled in minutes what two secondary summaries had left open, and exposed that the figure was never in the text at all.
- Changed: sources.md (11 rows, 6 new), claims.md (10 rows), legal-status.md (2 rows), 6 guide pages, CHANGELOG (8 index lines, 1 entry), TASKS, this file. Handoff 04 archived.
- Try next time: for any number pulled from a figure rather than text, write "from figure" in the source row on first entry.
