# Nashville Right-of-Way Permits - Machine Readable brief, 2026-11-12

Excavation permits are 31.0 percent of the records in Nashville's Active Right-of-Way Permits layer and hold 80.6 percent of the scheduled window-days (563,765 of 699,124). Lane closures are 54.3 percent of records at a median window of 6 days. Only 2,102 of 20,500 records (10.3 percent) have a scheduled window overlapping November 12, 2026, and the layer's Onstreet, Council District, and ZIP fields are populated on 6 of 20,500 records.

Full brief: brief-draft.md. Headline graphic: hero.png.

## Contents
- brief-draft.md - the brief
- stats.json - every headline figure with its population printed
- charts/ - family window-day shares, duration buckets, snapshot overlap, geography field population
- data/ - panels, the raw snapshot CSV, the pre-flight audit output, the pull log, the source layer metadata, and the independent verifier output
- code/ - pull_data.py, audit_section10.py, build_stats.py, verify_independent.py, charts.py, hero_composite.py
- verification.md - pre-flight audit, methods checklist, sync gate, story gate
- sources.md, reviewer-notes.md, social-drafts.md

## Reproduce
```
python3 code/pull_data.py
python3 code/audit_section10.py
python3 code/build_stats.py
python3 code/verify_independent.py
python3 code/charts.py
python3 code/hero_composite.py
```
Dependencies (matching the code's actual imports): Python 3 standard library plus pandas (verifier only), matplotlib (charts only), and Pillow (hero composite only). The pull, audit, and build scripts use only the standard library.

## Source
Active Right-of-Way Permits (Active_Right-of-Way_Permits), Metropolitan Government of Nashville and Davidson County via the Nashville Open Data Portal, ArcGIS FeatureServer layer 0 (services2.arcgis.com/HdTo6HJqh92wn4D8). Snapshot November 12, 2026.

## License
Brief text and derived data products: CC BY 4.0 (see LICENSE). Underlying records are Metro Nashville government open data.

Part of Machine Readable: https://adowlen.github.io/machine-readable/
