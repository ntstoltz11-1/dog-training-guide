# Handoff 03 : Verification pass 2 done, core studies confirmed with seven corrections

**Date:** 2026-10-08.

## Where things stand

- **Verified against primary sources (28 of 55):** session 03 added the twelve core comparative studies, S-01, S-02, S-03, S-07, S-08, S-09, S-10, S-11, S-12, S-17, S-18, S-19. All located by DOI or PubMed. No grade changed.
- **Seven corrections logged** in [`maintainers/CHANGELOG.md`](CHANGELOG.md). Largest: S-09 was mis-attributed ("Elliffe"; it is Sargisson and McLean 2021), and the old claim that the critique "did not reverse" the recall finding had no basis. C-34 now says the finding is disputed. S-07 and S-08 are one 63-dog dataset. S-18 had eleven wrong co-authors.
- **Guide pages edited:** 02/overview, 02/balanced, 02/dominance, 03/recall, 03/aggression, 03/separation, 05/breed, 01/common-myths, 06/medication-conversation. Reader wording now matches the studies.
- **Two full-text checks still open** (TASKS priority 1): Herron 2009 Fig. 3 reward-method figures; Simpson 2007 trial counts (242/197 vs FDA 229/188).
- **Pushed to GitHub 2026-10-08:** public at https://github.com/ntstoltz11-1/dog-training-guide. All page references converted to relative Markdown links (`maintainers/linkify.py`; rerun after adding pages). Every session now ends with `git add .`, `git commit`, `git push`.

## Next session

1. **Formatting and cleanup pass.** Use Claude in Chrome to open the live repo and screenshot the README, a method page, a problem page, a protocol card, and `evidence/sources.md`. Fix what renders badly: table widths, heading levels, code-styled link text in "Related pages" (consider plain titles), any page over the 80-line budget. Decide whether to strip the local path and name from `CLAUDE.md` and the archived handoffs.
2. Verification pass 3: the two full-text follow-ups, then priority 2 (Demant, Meyer and Ladewig, Asher, Korpivaara 2017, Engel, Ziv, Guilherme Fernandes, Deldalle and Gaunet, AVSAB, certification bodies, European statutes).
3. Nick test-reads [`decision-tree.md`](../guide/01-start-here/decision-tree.md) and [`children-and-dogs.md`](../guide/03-problems/children-and-dogs.md) cold.
4. Consider body-language diagrams ([`TASKS.md`](TASKS.md) Build).

## Retro (session 03)

- Went wrong: the original research report carried a wrong author name (S-09), a wrong author list (S-18), two wrong numbers (38%, 23%), and one unsupported assertion ("did not reverse"). All sat in the guide for a day. Verification before expansion was the right call.
- Went right: the extended-research pass checked all twelve in one run with DOI and PubMed records, and surfaced the Cooper 2014 correction notice and the China 2020 author reply.
- Changed: sources.md (12 rows), claims.md (11 rows plus header line), 9 guide pages, CHANGELOG (7 index lines, 1 entry), TASKS, this file. Handoff 02 archived.
- Try next time: when a research report gives a secondary-source number, mark it as such in the claim's Notes on first entry, so the verification queue is honest from day one.
