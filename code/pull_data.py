import urllib.request, urllib.parse, json, csv, time, os
BASE="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Active_Right-of-Way_Permits/FeatureServer/0/query"
META="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Active_Right-of-Way_Permits/FeatureServer/0?f=json"
DATA=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-row-permits-brief-2026-11-12/data")
def get(url):
    for a in range(5):
        try:
            with urllib.request.urlopen(url, timeout=90) as r: return json.load(r)
        except Exception as e:
            print("retry",e); time.sleep(3)
    raise RuntimeError("failed")
cnt=get(BASE+"?"+urllib.parse.urlencode({"where":"1=1","returnCountOnly":"true","f":"json"}))["count"]
print("server",cnt)
meta=get(META); json.dump(meta, open(os.path.join(DATA,"source-metadata-layer.json"),"w"), indent=2)
out=os.path.join(DATA,"nashville_row_raw.csv"); offset=0; total=0
with open(out,"w",newline="",encoding="utf-8") as f:
    w=None
    while True:
        params={"where":"1=1","outFields":"*","returnGeometry":"false","orderByFields":"ObjectId","resultOffset":offset,"resultRecordCount":1000,"f":"json"}
        j=get(BASE+"?"+urllib.parse.urlencode(params)); feats=j.get("features",[])
        if not feats: break
        for ft in feats:
            a=ft["attributes"]
            if w is None: w=csv.DictWriter(f, fieldnames=list(a.keys())); w.writeheader()
            w.writerow(a); total+=1
        print(total, flush=True)
        if not j.get("exceededTransferLimit"): break
        offset+=1000
print("DONE",total,cnt); assert total==cnt
json.dump({"source":BASE,"server_count":cnt,"rows":total,"pull_date":"2026-11-12"}, open(os.path.join(DATA,"pull_log.json"),"w"), indent=2)
