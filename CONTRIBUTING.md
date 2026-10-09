# Contributing

Thank you for wanting to improve this guide. Two kinds of contribution are welcome: corrections to what is here, and new content that meets the same standard.

## The standard

Every factual claim in `guide/` must trace to a row in `evidence/claims.md`, and every claim row must point to a source in `evidence/sources.md`. If you cannot source it, it does not go in. Opinions and experience are valuable, but they go in as "Consensus" or "Thin" with that label, never dressed up as research.

## Reporting a problem

Open an issue with:
- The file and the sentence
- What you think is wrong
- The primary source that supports the correction (a journal article, statute, or the organization's own page; not a blog or news summary)

Corrections to legal status need the statute or an official government page.

## Suggesting new content

Open an issue first describing the page or section. Check `maintainers/TASKS.md` to see if it is already planned.

## Making changes

1. Read `maintainers/writing-protocol.md`. Pages in `guide/` are for dog owners with no technical background: plain words, short paragraphs, the fixed template, under 80 lines, no author names or years in the body.
2. Use the templates in `guide/_templates/`.
3. For every new claim, add a row to `evidence/claims.md` and, if needed, `evidence/sources.md`, and put the claim IDs in the page footer.
4. Grade the claim per `maintainers/evidence-grading.md`. When in doubt, grade lower.
5. Never write a medication dose.
6. Any page touching bites, children, or aggression leads with safety and referral.
7. If your change reverses something the guide currently says, add an entry to `maintainers/CHANGELOG.md`.
8. Open a pull request. Describe what changed and why in plain language.

## Style

No em dashes. No emojis. Absolute dates (2026-10-08, not "last week"). Define any term on first use or link to `guide/01-start-here/glossary.md`.

## What we will not merge

- Recommendations for prong, choke, or shock collars, or dominance-based techniques. The evidence against them is summarized in `guide/02-methods/`; the guide's position on them is a locked decision.
- Claims without sources.
- Medication doses.
- Content that promotes a specific product, trainer, or business.

## License

By contributing you agree your work is released under the repository's license (CC BY-SA 4.0).
