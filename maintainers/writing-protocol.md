# Writing protocol

Two audiences, two rule sets. The folder decides which applies.

## `guide/` : written for dog owners

The test for every sentence: **could a tired person with a barking dog read this on a phone and know what to do?**

| Rule | Do | Do not |
|---|---|---|
| Plain words | "Reward the dog the moment it looks at you." | "Deliver the reinforcer contingent on orientation." |
| Define on first use | "Threshold (the distance at which your dog can still think and eat)." | Use a term from the glossary without a one-line definition or a link to [`glossary.md`](../guide/01-start-here/glossary.md). |
| Fixed template | Use `guide/_templates/`. Every section present; write "none" if empty. | Invent a page shape. |
| Short | Paragraphs of 1 to 3 sentences. Pages under 80 lines. | Walls of text. |
| Steps are numbered | "1. Stand 20 steps away. 2. When your dog looks at the trigger, say 'yes' and feed." | Prose instructions. |
| Numbers are starting points | "Start at about 5 seconds. Adjust to your dog." | Present a number as a rule. |
| Evidence label in words | "Evidence: Moderate." | Cite authors or years inside the page. |
| Footer only | Last line: `Evidence: C-01, C-03 (see evidence/claims.md)`. | Source tables inside the page. |
| Safety leads | Aggression, bites, children, muzzles: safety and referral come first. | Tips before safety. |
| No doses | "Ask your vet about fluoxetine." | Any mg or mg/kg. |
| Tone | Calm, direct, kind to the reader. Mistakes are normal. | Scolding, hype, or moralizing about methods. |

## `evidence/` and `maintainers/` : written for agents and Nick

| Rule | Do | Do not |
|---|---|---|
| Tables | One row per item, one line per row. | Prose. |
| IDs | Every claim `C-nn`, every source `S-nn`. | Unlabeled facts. |
| Dates act | Date every verdict, verification, and reversal. | "Updated" stamps on stable text. |
| One fact, one file | Write it where the [`CLAUDE.md`](../CLAUDE.md) routing table says; pointer elsewhere. | Restate across files. |
| Replace, never accumulate | Overwrite the superseded row; log the reversal in [`CHANGELOG.md`](CHANGELOG.md). | Strikethrough, "previously". |

## Everywhere

- No em dashes. Use commas, periods, or parentheses.
- No emojis.
- Absolute dates, `YYYY-MM-DD`.
- A verdict per item (apply / check first / hold / skip) with a short reason.
