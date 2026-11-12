import csv, json, os, collections, datetime, statistics
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,"..")); DATA=os.path.join(ROOT,"data")
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_row_raw.csv"),encoding="utf-8")))
def dt(v): return datetime.datetime.fromtimestamp(int(v)/1000, tz=datetime.timezone.utc) if v not in ("",None) else None
def fam(t):
    t=t or ""
    if "Bike Lane" in t: return "Bike Lane Closure"
    if "Excavation" in t: return "Excavation"
    if "Lane Closure" in t: return "Lane Closure"
    if "Sidewalk" in t: return "Sidewalk Closure"
    if "Street Closure" in t: return "Street Closure"
    if "Bike Lane" in t: return "Bike Lane Closure"
    return "Other"
def chan(t):
    t=t or ""
    if "Google" in t: return "Google-attributed"
    if "NDOT Project ONLY" in t: return "NDOT Project ONLY"
    return "Other / general"
for r in rows:
    r["_start"]=dt(r["Scheduled__Start"]); r["_end"]=dt(r["Scheduled__End"]); r["_init"]=dt(r["Initiated__Date"])
    r["_dur"]=(r["_end"]-r["_start"]).total_seconds()/86400
    r["_fam"]=fam(r["Permit__Type"]); r["_chan"]=chan(r["Permit__Type"])
    r["_company"]=(r["Company"] or "").strip() or "Blank"
pos=[r for r in rows if r["_dur"]>=0]; neg=[r for r in rows if r["_dur"]<0]
total_days=sum(r["_dur"] for r in pos)
snap=datetime.datetime(2026,11,12,tzinfo=datetime.timezone.utc)
overlap=[r for r in rows if r["_start"]<=snap<=r["_end"]]
ended=[r for r in rows if r["_end"]<snap]; future=[r for r in rows if r["_start"]>snap]
def agg(group_key, seq):
    out={}
    groups=collections.defaultdict(list)
    for r in seq: groups[group_key(r)].append(r)
    for k,v in sorted(groups.items(), key=lambda kv:-len(kv[1])):
        vd=[x for x in v if x["_dur"]>=0]
        out[k]={"n":len(v),"pct_of_all":round(len(v)/len(rows)*100,1),"median_days":round(statistics.median([x["_dur"] for x in vd]),2) if vd else None,"total_days":round(sum(x["_dur"] for x in vd),1),"total_days_pct":round(sum(x["_dur"] for x in vd)/total_days*100,1) if total_days else None,"overlap_nov12":sum(1 for x in v if x["_start"]<=snap<=x["_end"])}
    return out
stats={
 "dataset":"Nashville Active Right-of-Way Permits (Active_Right-of-Way_Permits, layer 0)",
 "snapshot_date":"2026-11-12","rows":len(rows),"server_count":20500,"unit":"one row = one permit record as served by the view",
 "status_counter":dict(collections.Counter(r["Status"] for r in rows)),
 "permit_type_counter":dict(collections.Counter(r["Permit__Type"] for r in rows)),
 "family":agg(lambda r:r["_fam"], rows),
 "channel":agg(lambda r:r["_chan"], rows),
 "company_top_by_n":agg(lambda r:r["_company"], rows),
 "duration":{"negative_n":len(neg),"zero_n":sum(1 for r in rows if r["_dur"]==0),"positive_n":len(pos)-sum(1 for r in rows if r["_dur"]==0),"median_days_all_nonneg":round(statistics.median([r["_dur"] for r in pos]),2),"total_days_nonneg":round(total_days,1),
   "buckets":{"0":sum(1 for r in rows if r["_dur"]==0),"1":sum(1 for r in rows if 0<r["_dur"]<=1),"2-7":sum(1 for r in rows if 1<r["_dur"]<=7),"8-30":sum(1 for r in rows if 7<r["_dur"]<=30),"31-91":sum(1 for r in rows if 30<r["_dur"]<=91),">91":sum(1 for r in rows if r["_dur"]>91),"negative":len(neg)}},
 "snapshot_overlap":{"overlap_nov12_2026":len(overlap),"overlap_pct":round(len(overlap)/len(rows)*100,1),"ended_before_nov12":len(ended),"ended_pct":round(len(ended)/len(rows)*100,1),"starting_after_nov12":len(future)},
 "geography_fields":{"Onstreet_populated":sum(1 for r in rows if r["Onstreet"]),"Council__District_populated":sum(1 for r in rows if r["Council__District"]),"Zip_populated":sum(1 for r in rows if r["Zip"]),"Fromstreet_populated":sum(1 for r in rows if r["Fromstreet"]),"Tostreet_populated":sum(1 for r in rows if r["Tostreet"]),"LatLon_degrees_populated":6,"LatLon_stateplane_populated":20491,"LatLon_blank":3},
 "days_to_work_counter":dict(collections.Counter(r["Days_to__Work"] or "Blank" for r in rows)),
 "company_blank_n":sum(1 for r in rows if r["_company"]=="Blank"),
 "permit_number_zero_n":sum(1 for r in rows if r["Permit__"]=="0"),
 "initiated_range":["2022-10-06","2026-11-10"],
 "fromstreet_top":dict(collections.Counter(r["Fromstreet"] for r in rows if r["Fromstreet"]).most_common(15)),
}
# trim company to top 15 by n for stats readability but keep full panel csv
stats["company_top_by_n"]={k:stats["company_top_by_n"][k] for k in list(stats["company_top_by_n"])[:15]}
json.dump(stats, open(os.path.join(ROOT,"stats.json"),"w"), indent=2)
# panels
def write_panel(name, d):
    with open(os.path.join(DATA,name),"w",newline="") as f:
        w=csv.writer(f); w.writerow(["group","n","pct_of_all","median_days","total_days","total_days_pct","overlap_nov12"])
        for k,v in d.items(): w.writerow([k,v["n"],v["pct_of_all"],v["median_days"],v["total_days"],v["total_days_pct"],v["overlap_nov12"]])
write_panel("family_panel.csv", agg(lambda r:r["_fam"], rows))
write_panel("company_panel.csv", agg(lambda r:r["_company"], rows))
write_panel("type_panel.csv", agg(lambda r:r["Permit__Type"], rows))
print(json.dumps({k:stats[k] for k in ["family","duration","snapshot_overlap","geography_fields"]}, indent=2))
