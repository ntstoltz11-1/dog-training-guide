# Verification protocol

How a source moves from Verified = N to Verified = Y in `evidence/sources.md`.

## Steps

1. **Locate the primary document.** Journal article (DOI or PubMed), statute text, or the organization's own position statement page. A blog summary or news article does not count as primary for a study or a law.
2. **Confirm four fields:** authors and year, journal or issuing body, the specific finding as stated in `claims.md`, and sample size or scope.
3. **Check for corrections.** Search the title plus "correction", "erratum", "retraction", and for a published commentary or critique. Record any in the claim's Notes column.
4. **Compare the claim to the finding.** If the claim overstates, rewrite the claim to match. Regrade per `evidence-grading.md`.
5. **Update `sources.md`:** Verified = Y, date, and the primary link.
6. **Update `claims.md`:** verified date; grade if changed.
7. **Update the guide pages** listed in the claim's "Used in" column if the label or wording changed.
8. **Remove the `TASKS.md` row.** If the grade changed, add a `CHANGELOG.md` entry.

## Source types and what counts as primary

| Type | Primary |
|---|---|
| Peer-reviewed study | Journal page (DOI) or PubMed Central full text |
| Position statement | The organization's own website (AVSAB, ESVCE, BVA, ACVB) |
| Law or regulation | Government legislation site (legislation.gov.uk, gov.wales, parliament record) |
| Practitioner protocol | The author's published book or official course page |
| Certification requirement | The certifying body's current requirements page, dated |

## Legal facts

Legal rows in `legal-status.md` are never marked High confidence from a news article or a retailer blog. High requires the statute or an official government page. Record the date checked; legal status changes.
