# Verification - Nashville Active Right-of-Way Permits, 2026-11-12

## Pre-flight audit
Script: code/audit_section10.py. Output: data/audit_output.txt. Result: PASS (assert rows == 20,500 held; all checks below recorded from that output).

- Zero/null sentinel handling: Permit number 0 occurs on 20 records; treated as a placeholder number, excluded only from distinct-number statements, records retained. Negative scheduled windows (17 records) are excluded from window-day totals and medians and reported as a count; zero windows (1,091) are retained and bucketed separately. Unknown or blank categories are never placed in a rate denominator silently: geography field shares use the full 20,500 denominator, with populated counts printed.
- Polarity check (matched vs excluded sample): audit prints 3 negative-duration records (excluded from sums) and 3 non-negative records (included); the code keeps duration >= 0 in sums and medians, which matches the stated intent.
- Numerator/denominator unit agreement: every rate is permit records over permit records, or window-days over window-days, on the same record population. No cross-unit rate is computed.
- Categorical exhaustiveness: the audit records a Counter of all unique values for every column used in a grouping or filter: Permit Type (24 values), Status (2), Company (top 30 printed, full panel in data/company_panel.csv), Days_to_Work (6 values including blank), and City (3). Family grouping is by substring with the Bike Lane check ordered before Lane Closure, verified against the type counter: families sum to 20,500.
- Nullable denominator: geography shares are computed on the full 20,500; determined plus not-determined counts sum to the whole for each field (for example Onstreet 6 populated plus 20,494 blank).

## Join hygiene (Section 10.2)
- No spatial or relational join is used in the published figures. The planned council-district join and crash-layer join were cut: Council District is populated on 6 of 20,500 records and Lat/Lon on the NDOT-era records hold State Plane feet, not degrees, so no proximity or name-matched rate can be computed honestly from the layer as published. That cut is the layering admission result: the crash layer could not support a claim this brief could not otherwise make, because the shared geography does not exist in usable form.
- Physical scale: window-day totals are printed alongside record counts throughout, so permit counts are never read as street length; the brief states that no street-mile denominator exists in the layer.
- Built-in internal control group: the 6 legacy Status ACTIVE records. They populate Onstreet, Council District, and ZIP (6 of 6), carry degree coordinates (6 of 6), and use the older type strings, while the 20,494 ISSUE records populate none of those fields (0 of 20,494). Field population follows record vintage exactly, which is the evidence that the blanks are systematic to how the NDOT-era records are served rather than random missing entries.

## Methods checklist (Section 3 of the standards)
- Base rates and exposure: no exposure denominator exists in the layer (no street miles, lane miles, or traffic). Stated prominently in the brief's second paragraph; no network share and no causal pattern is claimed.
- Direction of causality: considered and printed in Methods and What this might mean; scheduled windows are not treated as observed disruption.
- Category and definition changes: the legacy versus NDOT-era type strings and field systems are documented; initiated-date stock is concentrated in 2025-2026, so no long trend is printed.
- Exact date range: snapshot November 12, 2026; initiated dates October 6, 2022 to November 10, 2026 as recorded. The timely decision named is the Metro Council meeting of November 17, 2026, which falls after the snapshot.
- Join match rates: no joins used; see Join hygiene.
- Small counts: smallest family printed is Other (60 records); type strings with 1 to 15 records appear only in the full counter, not as standalone percentage claims, except their printed shares of the full layer in stats.json.
- Official definitions: the layer metadata defines none of the type, channel, or status labels used; the brief reports labels as recorded and assigns no definition the metadata does not carry, including the Google attribution.

## Independent verification
Script: code/verify_independent.py (separate pandas implementation). Output: data/verify_independent_output.json. All 8 checks pass: row count 20,500; excavation count 6,348; excavation window-day share 80.6 percent within 0.15 points; snapshot overlap 2,102; Onstreet populated 6; ERVIN CABLE CONSTRUCTION LLC 5,893 records; negative windows 17; non-negative median window 13.0 days. Live server count re-read in the pull log: 20,500, equal to the pulled rows.

## Sync gate (Section 10.3)
- README dependency list matches code imports: standard library for pull, audit, and build; pandas for the verifier only; matplotlib for charts only; Pillow for the hero composite only.
- Every number in brief-draft.md was cross-checked against stats.json after the final build_stats run, including the derived two-holder window-day total (217,268 plus 166,115 equals 383,382, which is 54.8 percent of 699,124) and the overlap family counts (1,421 plus 463 plus 151 plus 27 plus 14 plus 26 equals 2,102).

## Story gate (Section 13)
- Thesis (recorded in reviewer-notes.md before final prose): the register is dominated in count by short lane closures and in scheduled window-days by about-90-day excavations held by a small number of holders, and its named geography fields are blank on the NDOT-era records, so the district and street accounting the study design asked for cannot be produced from the layer as published.
- Cold reader (fresh agent, saw only brief-draft.md): returned point - "Although most of Nashville's active right-of-way permit records are short lane closures, excavations dominate the total scheduled time, and the layer's location and 'active' fields are not usable as published to show where or whether work is actually happening on a given day." That matches the recorded thesis in substance. Most memorable number: 80.6 percent, the excavation share of window-days, which is the headline finding. Where it got bored or lost: the "How long the windows run" section, specifically the channel medians, because the Google label is unexplained and the split did not connect back to the excavation story. Disposition: the section is retained because the channel split documents that the Google label is recorded but undefined, a caveat a data user needs; no figure changes, and the bored point is recorded here as the story gate requires. The gate's pass conditions (point produced and matching, memorable number is the headline) are met.
- Human-scale conversion: the headline carries two, labeled derived - about 1 in 3 records is an excavation carrying about 4 in 5 window-days, and the excavation window-day total is expressed as about 1,544 years of a single permit window, with the overlap warning printed in the same sentence.

## Privacy check
The raw snapshot contains street segment descriptions, company names, and applicant names as published by Metro in the open layer. Applicant names are not reproduced in the brief; company names are organizational holders as recorded. No personal contact data is in the layer.
