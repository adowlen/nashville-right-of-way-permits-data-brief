# Sources - Nashville Active Right-of-Way Permits brief, 2026-11-12

Primary source for every figure: Active Right-of-Way Permits (Active_Right-of-Way_Permits), Metropolitan Government of Nashville and Davidson County via the Nashville Open Data Portal, ArcGIS FeatureServer layer 0, services2.arcgis.com/HdTo6HJqh92wn4D8. Snapshot pulled November 12, 2026; server count 20,500, pulled count 20,500. Layer metadata archived at data/source-metadata-layer.json; pull log at data/pull_log.json.

- Record total, status counter, permit type counter: counts of the pulled records, stats.json.
- Family, channel, and company figures: derived from the recorded Permit Type and Company strings on the pulled records; grouping rules in brief Methods; panels at data/family_panel.csv, data/type_panel.csv, and data/company_panel.csv. Derived.
- Scheduled windows and window-days: derived from Scheduled Start and Scheduled End timestamps on each record (End minus Start, days). Negative windows (17 records) excluded from totals and medians. Derived.
- Snapshot overlap (2,102 records overlapping November 12, 2026): derived by comparing each record's scheduled window with that date.
- Geography field population (Onstreet, Council District, ZIP, Fromstreet, Tostreet, Lat, Lon): counts of populated values on the pulled records. The State Plane reading of Lat and Lon on NDOT-era records is based on the values themselves (northing values near 660,000 and easting values near 1,740,000, in feet, against degree coordinates on the 6 legacy records).
- Days_to_Work values: counter of the recorded field, stats.json.
- Crash-layer comparison: not computed; the comparison layer is the Nashville Traffic Accidents layer as published in Machine Readable's November 2, 2026 brief (adowlen/nashville-traffic-accidents-data-brief). The cut and its reason are recorded in verification.md.
- Metro Council November 17, 2026 meeting date: from the pick record in hidden_files/leads_log.md (CHOSEN BY ALEX line, 2026-11-11), which names that meeting as a timely hook for this brief.
