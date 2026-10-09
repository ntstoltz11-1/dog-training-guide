# Evidence grading

Every claim in [`evidence/claims.md`](../evidence/claims.md) carries one grade. The grade appears in words on every guide page that uses the claim.

## The four grades

| Grade | Criteria | Reader-facing wording |
|---|---|---|
| **Strong** | Two or more independent studies agree, or at least one randomized controlled trial with adequate sample, or a large well-powered dataset. | "Strong: several good studies agree." |
| **Moderate** | One controlled study, or several consistent observational studies, or a published methodological critique exists but the direction of the finding holds. | "Moderate: supported by one controlled study or consistent surveys." |
| **Consensus** | Position statement from AVSAB, ACVB, ESVCE, BVA, or equivalent; or a protocol taught by certified bodies (IAABC, CCPDT, KPA) with no controlled trial. | "Consensus: experts agree, no formal trial." |
| **Thin** | Case report, one small study (under about 30 subjects), practitioner anecdote, or no source located. | "Thin: a starting point, not a rule." |

## Rules

1. Grade the **claim**, not the study. A strong study can support a thin claim if the claim goes beyond what was tested.
2. Correlational findings cap at **Moderate** no matter how many agree, because owners self-select methods.
3. A **published critique** does not lower the grade by itself; it is recorded in the claim's Notes column. If the critique overturns the finding, the grade changes and [`CHANGELOG.md`](CHANGELOG.md) gets an entry.
4. **Laboratory or working-dog samples** get a Notes flag ("lab dogs" or "guide-dog candidates") because generalization to pet dogs is inferred.
5. **Legal facts** are not graded. They carry a confidence level (High / Moderate / Low) and a last-verified date in [`evidence/legal-status.md`](../evidence/legal-status.md).
6. **Numbers in protocol cards** (seconds, repetitions, distances) default to Consensus unless a study tested that number.
7. When two sources **disagree**, the claim states both and the grade reflects the weaker side. The disagreement is named on the guide page in one sentence.

## Downgrade triggers

| Trigger | Action |
|---|---|
| Source cannot be located on verification | Grade drops to Thin; [`TASKS.md`](TASKS.md) row; guide page label updated |
| Retraction or failed replication found | Grade reassessed; [`CHANGELOG.md`](CHANGELOG.md) entry |
| Claim found to overstate the study | Rewrite claim to match the study; regrade |
