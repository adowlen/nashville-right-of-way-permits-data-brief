# Reviewer notes - Nashville Active Right-of-Way Permits, 2026-11-12

Thesis (recorded before final prose, from the pre-analysis data profile): The active right-of-way register is dominated in count by short lane closures and in scheduled window-days by about-90-day excavations held by a small number of holders, and its named geography fields are blank on the NDOT-era records, so the district and street accounting the study design asked for cannot be produced from the layer as published.

Claims most likely to be challenged:
- Window-days are scheduled permit windows, not observed work or observed closures. The brief states this in the scale paragraph, in What this might mean (with the strongest alternative explanation), and in Caveats. Any reader who treats 90-day windows as 90 days of digging will overread the finding; the wording was built against that reading.
- The State Plane reading of Lat and Lon: it rests on the values themselves (six-figure northing, seven-figure easting) and on the contrast with the 6 legacy records carrying degrees. It is stated as a reading of the served values, not as a publisher statement; NDOT could confirm or correct it, and the brief's Who can act asks the publisher to publish the coordinate reference.
- The Google-attributed channel label: the metadata does not define it, and the brief assigns it no meaning. A challenger with the program documentation could add context the brief deliberately does not guess at.
- Company concentration uses the recorded Company string, not a normalized holder ID; variant strings could move holder totals. Blank company is 1,897 records (9.3 percent) and is printed.

Methods checks that could not be completed:
- Council-district analysis: impossible from the layer as published (district populated on 6 of 20,500). Cut, not estimated.
- Crash-layer comparison from the original study design: cut, because there is no usable shared geography key for the NDOT-era records. Recorded in verification.md under the layering admission test.
- Exposure normalization: no street-mile, lane-mile, or traffic denominator exists in the layer; the brief says so prominently and computes no network share.

Surprising findings:
- Onstreet, Council District, and ZIP are populated on exactly the same 6 records, and those are the only Status ACTIVE records and the only degree-coordinate records: three separate field systems all split on the same vintage line.
- The layer total (20,500) overstates work scheduled for the snapshot day by about ten times against the window-overlap count (2,102), because 89.7 percent of windows had already ended.
- Days_to_Work, which the bank lead's field list suggested might be a duration, is a weekday-pattern field.

No finding in this brief reflects badly on a named individual. The publisher-level findings (blank fields, coordinate units, Status semantics) name NDOT as the layer publisher in the Who can act section, in measured terms, with baselines and the outcome measure that would show a fix.
