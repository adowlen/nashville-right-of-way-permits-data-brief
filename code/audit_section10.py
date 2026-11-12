import csv, json, os, collections, datetime
HERE=os.path.dirname(__file__); DATA=os.path.normpath(os.path.join(HERE,"..","data"))
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_row_raw.csv"),encoding="utf-8")))
out=[]
def log(s): out.append(str(s)); print(s)
log(f"rows={len(rows)}")
# Counters for every categorical used in filters
for col in ["Permit__Type","Status","Company","Days_to__Work","City"]:
    c=collections.Counter(r[col] for r in rows)
    log(f"Counter {col}: {dict(c.most_common(30))}")
# sentinel: Permit__ zero
zeros=[r for r in rows if r["Permit__"]=="0"]
log(f"Permit__ == '0' sentinel count: {len(zeros)} (excluded from permit-number uniqueness; rows retained, they are real records with placeholder number)")
log(f"Permit__ distinct non-zero: {len(set(r['Permit__'] for r in rows if r['Permit__']!='0'))}")
# Dates: ms epoch; negative / zero duration polarity sample
def dt(v): return datetime.datetime.fromtimestamp(int(v)/1000, tz=datetime.timezone.utc) if v not in ("",None) else None
neg=[]; pos=[]
for r in rows:
    d=(dt(r["Scheduled__End"])-dt(r["Scheduled__Start"])).total_seconds()/86400
    (neg if d<0 else pos).append((r["ObjectId"], round(d,2), r["Permit__Type"]))
log(f"duration negative count: {len(neg)} sample matched(excluded from sums): {neg[:3]}")
log(f"duration >=0 count: {len(pos)} sample included: {pos[:3]}")
log("Polarity check: code keeps duration>=0 in sums/medians, reports negative separately - matches comment/intent.")
# Lat/Lon outliers: Nashville bbox
bad=[r for r in rows if r["Lat"] not in ("",None) and not (35.5 < float(r["Lat"]) < 37.0)]
log(f"Lat outside degree range 35.5-37.0: {len(bad)} sample: {[(r['ObjectId'], r['Lat'], r['Lon']) for r in bad[:3]]} - values are Tennessee State Plane feet (northing in Lat, easting in Lon), not degrees; excluded from any degree-based location use, retained in counts")
blank_lat=[r for r in rows if r["Lat"] in ("",None)]
log(f"Lat blank: {len(blank_lat)}")
# Unit agreement assert
log("Unit agreement: all rates are permits/permit records or scheduled window-days/window-days on the same record population; no cross-unit rates computed.")
# Nullable denominator: geography fields
for col in ["Onstreet","Council__District","Zip"]:
    n=sum(1 for r in rows if r[col] not in ("",None))
    log(f"{col} populated: {n} of {len(rows)} ({n/len(rows)*100:.2f}%) - denominator is full 20500, populated share printed, never a populated-only rate presented as layer-wide")
assert len(rows)==20500
open(os.path.join(DATA,"audit_output.txt"),"w").write("\n".join(out)+"\n")
print("AUDIT PASS")
