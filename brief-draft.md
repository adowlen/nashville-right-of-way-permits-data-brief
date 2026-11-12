# Nashville right-of-way permits: excavations are 31.0 percent of the records and 80.6 percent of the scheduled window-days

**One-line summary:** Of the 20,500 records in Nashville's Active Right-of-Way Permits layer on November 12, 2026, 11,132 (54.3 percent) are lane closures with a median scheduled window of 6 days, while 6,348 (31.0 percent) are excavations with a median window of about 90 days, so excavations hold 563,765 of the 699,124 non-negative scheduled window-days (80.6 percent, derived); only 2,102 records (10.3 percent) have a scheduled window that overlaps November 12, 2026.

Start with the scale. Machine Readable pulled the full layer from Metro's ArcGIS service on November 12, 2026; the pulled row count matches the server's own count exactly (20,500). One row is one permit record. Scheduled window means Scheduled End minus Scheduled Start on that record, in days. Window-days are added across records, so overlapping permits count separately; the total is a measure of permitted window load, not calendar time and not street length. No exposure denominator exists in the layer - there is no street-mile, lane-mile, or traffic volume field - so this brief reports counts, shares of records, and shares of window-days, and makes no claim about how much of Nashville's street network is affected.

## What the register holds, by family

Permit types are grouped by the work named in the type string. The full counter of all 24 recorded type strings is in stats.json.

- Lane Closure: 11,132 records (54.3 percent), median window 6.0 days, 99,640 window-days (14.3 percent).
- Excavation: 6,348 records (31.0 percent), median window 90.04 days, 563,765 window-days (80.6 percent).
- Sidewalk Closure: 2,324 records (11.3 percent), median window 6.0 days, 22,090 window-days (3.2 percent).
- Street Closure: 506 records (2.5 percent), median window 12.48 days, 7,492 window-days (1.1 percent).
- Bike Lane Closure: 130 records (0.6 percent), median window 6.0 days, 1,475 window-days (0.2 percent).
- Other types: 60 records (0.3 percent), 4,661 window-days (0.7 percent).

Human scale (derived): about 1 in 3 records is an excavation, and those records carry about 4 in 5 of the scheduled window-days. The 563,765 excavation window-days are the equivalent of about 1,544 years of a single permit window; windows overlap, so that figure is a load comparison, not a timeline.

## How long the windows run

- Across the 20,483 records with a non-negative window, the median scheduled window is 13.0 days and the total is 699,124 window-days (derived, rounded).
- Window lengths cluster at the short end and at about 90 days: 1,091 records run 0 days, 426 run 1 day, 6,775 run 2 to 7 days, 5,565 run 8 to 30 days, 6,337 run 31 to 91 days, and 289 run more than 91 days.
- 17 records carry a negative window (Scheduled End before Scheduled Start). They are excluded from every window-day total and median in this brief and are counted here and in the audit.
- By the channel named in the type string, NDOT Project ONLY records (7,113, 34.7 percent) run a median of 4.0 days, Google-attributed records (6,292, 30.7 percent) a median of 13.0 days, and the remaining general records (7,095, 34.6 percent) a median of 90.0 days. The layer metadata does not define the Google attribution, so this brief reports it as a recorded label and assigns it no meaning beyond the label.
- Days_to_Work does not record a duration. Its recorded values are weekday patterns: Monday - Friday Only on 9,205 records, Monday - Saturday Only on 6,880, blank on 4,401, and three other patterns on 14 records combined. No duration figure in this brief uses that field.

## Who holds the permits

Company is recorded on 18,603 records and blank on 1,897 (9.3 percent). Company figures are shares of all 20,500 records unless a different base is printed.

- ERVIN CABLE CONSTRUCTION LLC holds the most records: 5,893 (28.7 percent), median window 13.0 days, 166,115 window-days (23.8 percent).
- METRO WS INTERNAL DEPT holds 2,443 records (11.9 percent), median window 90.0 days, and the most window-days of any holder: 217,268 (31.1 percent).
- GIBBS, SAMMIE DBA SAMMIE GIBBS CONSTRUCTION holds 1,908 records (9.3 percent), median window 4.0 days, 7,551 window-days (1.1 percent).
- GOODWIN, ROY T CONTRACTORS INC holds 1,865 records (9.1 percent) and C K MASONRY CO INC holds 1,158 (5.6 percent).
- Together, the two largest holders by window-days (METRO WS INTERNAL DEPT and ERVIN CABLE CONSTRUCTION LLC) hold 383,382 window-days, 54.8 percent of the total (derived from the figures above).

## What "Active" means in this layer

Status is recorded as ISSUE on 20,494 records and ACTIVE on 6 records. Against the snapshot date:

- 2,102 records (10.3 percent) have a scheduled window that overlaps November 12, 2026: 1,421 excavations, 463 lane closures, 151 sidewalk closures, 27 street closures, 14 bike lane closures, and 26 other records.
- 18,391 records (89.7 percent) have a Scheduled End before November 12, 2026.
- 7 records have a Scheduled Start after November 12, 2026.

The layer name and the Status field therefore do not, on their own, produce a list of work scheduled for a given day; the scheduled dates do. A reader who filtered on Status alone would return either 6 records or 20,494 records, neither of which is the 2,102-record overlap count.

## The geography fields, as published

- Onstreet is populated on 6 of 20,500 records (0.03 percent). Council District is populated on 6 of 20,500. ZIP is populated on 6 of 20,500.
- The 6 populated records are the 6 records with Status ACTIVE. They carry the layer's older type strings (for example EXCAVATION PERMIT and LANE CLOSURE, without the NDOT prefix) and real degree coordinates. None of the 20,494 ISSUE records populates Onstreet, Council District, or ZIP. This is the brief's built-in control: field population follows record vintage exactly, so the blanks are a property of how the NDOT-era records are served, not random missing entries.
- Fromstreet is populated on 20,394 records and Tostreet on 18,917, so segment descriptions exist for most records. The most common Fromstreet values include Dead End (249 records), Murfreesboro Pike (126), Lebanon Pike (93), Nolensville Pike (92), and Gallatin Pike (88). Fromstreet is a segment endpoint as recorded, not a standardized street assignment, and spelling variants occur (Nolensville Pike 92 and Nolensville Pk 61 are counted separately in the panel), so this brief does not rank streets by window-days.
- Lat and Lon are populated on 20,497 records, but on the 20,491 NDOT-era records with coordinates they hold Tennessee State Plane feet values (a northing in the Lat field and an easting in the Lon field), not degrees. Only the 6 legacy ACTIVE records hold degree coordinates. This brief makes no map and no district or neighborhood figure from those fields as published.
- Because Council District is blank on the NDOT-era records, the council-district question in the original study design cannot be answered from this layer as published, and no district figure is printed. The crash-layer comparison in the original design is likewise not computed: the published crash layer (Machine Readable, November 2, 2026) is organized by precinct and coordinates, and this layer carries no usable district or degree-coordinate field for the NDOT-era records to join on. Both cuts are recorded in the verification file.

## What this might mean

One possible reading is that permitted right-of-way load in Nashville, measured in scheduled window-days, is mainly an excavation load held by a small number of holders, while the day-to-day count of permits is mainly short lane closures. The strongest alternative explanation is that scheduled windows are permit validity windows rather than days of actual work on the street: a 90-day excavation window does not show that work, or a closure, was present on each of those days, and the layer records no actual start or completion. On the data as published, the window-day figures measure permitted windows, and any use that needs actual work days or actual closures needs a field this layer does not carry.

## Who can act

- **NDOT (Nashville Department of Transportation and Multimodal Infrastructure), as the layer publisher:** populate Onstreet, Council District, and ZIP for NDOT-era records, or publish a note in the layer metadata stating why those fields are blank and which fields should be used for location instead. Cost class: low-cost operational change (metadata and export configuration, no new collection implied by this brief). Outcome measure: the populated share of those three fields on the next pull of this layer, against the November 12, 2026 baseline of 6 of 20,500 for each.
- **NDOT:** publish the coordinate reference for the Lat and Lon fields as served, or serve degree coordinates in those fields. Cost class: low-cost operational change. Outcome measure: the share of records whose Lat value falls in the degree range for Nashville on the next pull, against the baseline of 6 of 20,500.
- **Metro Council, ahead of its November 17, 2026 meeting, and NDOT:** when using this layer to describe current work, use the scheduled-window overlap count for the date in question (2,102 records for November 12, 2026) rather than the layer total or the Status field. Cost class: low-cost operational change. Outcome measure: council or NDOT reporting that prints an overlap count with its date; the dataset that would show the underlying change is this same layer on a later pull.
- **NDOT:** add or publish an actual-work indicator if one is collected (for example actual start and completion dates), so scheduled windows can be separated from work performed. Cost class: budget decision if it requires system changes; the brief does not estimate a figure. Outcome measure: the share of records carrying an actual date field on a future pull.

## Methods

- Source: Active Right-of-Way Permits (Active_Right-of-Way_Permits), Metropolitan Government of Nashville and Davidson County via the Nashville Open Data Portal, ArcGIS FeatureServer layer 0 (services2.arcgis.com/HdTo6HJqh92wn4D8). Snapshot November 12, 2026; pulled count 20,500 equals the server count.
- Families group the 24 recorded Permit Type strings by the work word in the string (Excavation, Lane Closure, Sidewalk Closure, Street Closure, Bike Lane Closure, other). The Bike Lane check runs before the Lane Closure check so bike lane records are not counted as lane closures. Channel groups the same strings by the suffix label (Google, NDOT Project ONLY, neither).
- Durations are Scheduled End minus Scheduled Start in days, computed from the millisecond timestamps as served. Negative durations (17 records) are excluded from totals and medians and reported as their own count. Zero-duration records (1,091) are retained.
- Exposure: no street-mile, lane-mile, traffic, or population denominator exists in the layer, so no rate per mile or per resident is computed and no causal pattern is implied.
- Causality direction: longer windows for excavations are a property of the permit records; this brief does not claim excavations cause more disruption per day, because no per-day presence or closure field exists.
- Category and definition changes: the 6 legacy ACTIVE records use older type strings and populate fields the NDOT-era records do not; they are retained in all totals (they are 0.03 percent of records) and used as the control described above. Initiated dates in the layer run from October 6, 2022 to November 10, 2026, but the record stock is concentrated in 2025 (8,501 initiated) and 2026 (11,263 initiated), so no year trend is printed.
- Joins: no dataset join is used in the published figures. The planned district and crash joins were cut for the reasons printed in the geography section; the cut is the layering admission result for this brief.
- Small counts: groups under about 30 records (Other family, 60 records, is the smallest family printed; individual type strings with 1 to 15 records) are reported as counts in the counter and are not given standalone percentage claims in the prose beyond their share of the full layer.

## Caveats

- Scheduled windows are not observed work. Nothing in the layer shows that work started, finished, or closed anything on a particular day inside its window.
- Company is a recorded string, not a normalized holder identifier; holders may also appear under variant strings, and 1,897 records carry no company.
- Permit numbers: 20 records carry Permit number 0, which reads as a placeholder; those records are retained in every count and the placeholder is excluded only from any statement about distinct permit numbers (20,480 distinct non-zero numbers).
- The snapshot is a single day. The layer is a live register; counts will drift as permits are added and windows pass.

Sources for every figure are in sources.md. The pre-flight audit, independent verification, and story gate are in verification.md.
