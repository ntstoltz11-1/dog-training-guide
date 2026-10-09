# Page build procedure

How an agent turns evidence into a `guide/` page. Run in order.

1. **Pick the template.** `guide/_templates/_TEMPLATE-problem.md`, `_TEMPLATE-method.md`, or `_TEMPLATE-protocol.md`. Copy it to the right folder with a lowercase hyphenated name.
2. **List the claims first.** Before writing prose, list every factual claim the page will make. For each, find or create its `C-nn` row in `evidence/claims.md`. If no source exists, either search and add an `S-nn` row or leave the claim out.
3. **Set the page's evidence label.** The label at the top of the page is the grade of the page's central recommendation, not the average of all claims.
4. **Write the "Do this" section first.** Steps, numbered, in the order a reader performs them. Each step one action. Then write the rest around it.
5. **Write "Avoid this" from the failure modes** recorded in the research or claims Notes column. Each item one line: the mistake, then why it backfires.
6. **Write "Get help if"** with concrete triggers (a bite, no progress after N weeks, children in the home), and point to `guide/01-start-here/when-to-get-help.md`.
7. **Cross-link.** Any technique longer than 10 lines points to its `guide/04-protocols/` card. Any term not in everyday English links to `glossary.md`.
8. **Footer.** Last line: `Evidence: C-nn, C-nn (see evidence/claims.md)`. Nothing else below it.
9. **Readability pass.** Read every sentence aloud in your head as a tired dog owner on a phone. Cut any sentence that does not change what they do.
10. **Budget check.** Under 80 lines. If over, move steps to a protocol card.
11. **Update `claims.md`.** Add the page path to the "Used in" column of every claim cited.
12. **Update routing** if the page is a reader entry point: `README.md` table.

## Page quality checklist

- [ ] Every section of the template is present
- [ ] No author names or years in the body
- [ ] Every number labeled as a starting point unless study-backed
- [ ] Safety and referral content appears before technique on any aggression-adjacent page
- [ ] No medication dose anywhere
- [ ] Footer claim IDs all exist in `claims.md`
- [ ] Under 80 lines
