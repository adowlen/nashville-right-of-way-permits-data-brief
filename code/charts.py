import json, os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,".."))
stats=json.load(open(os.path.join(ROOT,"stats.json")))
plt.rcParams.update({"font.size":10,"axes.facecolor":"white"})
AMBER="#E8A317"; TEAL="#0E7C7B"; CHAR="#222222"
def save(fig,name):
    fig.tight_layout(); fig.savefig(os.path.join(ROOT,"charts",name), dpi=200); plt.close(fig); print(name)
# family total days vs count
fam=stats["family"]; labels=list(fam); ns=[fam[k]["total_days_pct"] for k in labels]; counts=[fam[k]["pct_of_all"] for k in labels]
fig,ax=plt.subplots(figsize=(8,4.2)); y=range(len(labels))
ax.barh(y, ns, color=TEAL, label="Share of scheduled window-days")
ax.barh([i+0.0 for i in y], counts, color=AMBER, alpha=0.0)
for i,k in enumerate(labels): ax.text(ns[i]+1,i,f"{ns[i]}% of days, {counts[i]}% of permits",va="center",fontsize=9)
ax.set_yticks(list(y)); ax.set_yticklabels(labels); ax.invert_yaxis(); ax.set_xlabel("Percent"); ax.set_title("Excavation permits hold most scheduled window-days\nNashville active right-of-way permits, snapshot Nov 12, 2026"); ax.set_xlim(0,118)
fig.text(0.01, -0.02, "Source: Metro Nashville Active Right-of-Way Permits layer, 20,500 records. Window-days are Scheduled End minus Start, negative durations (17) excluded.", fontsize=7, ha="left")
save(fig,"chart_family_days.png")
# duration buckets
b=stats["duration"]["buckets"]; labels2=["0","1","2-7","8-30","31-91",">91"]; vals=[b[k] for k in labels2]
fig,ax=plt.subplots(figsize=(8,4.2)); ax.bar(labels2, vals, color=AMBER)
for i,v in enumerate(vals): ax.text(i,v+120,str(v),ha="center",fontsize=9)
ax.set_ylabel("Permit records"); ax.set_xlabel("Scheduled window length (days)"); ax.set_title("Scheduled windows cluster at short closures and at about 90 days")
fig.text(0.01,-0.02,"17 records with a negative window are excluded from this chart and reported in the brief.",fontsize=7)
save(fig,"chart_duration_buckets.png")
# snapshot overlap
fig,ax=plt.subplots(figsize=(8,3.8)); ax.barh(["Window ended before Nov 12, 2026","Window overlaps Nov 12, 2026","Window starts after Nov 12, 2026"],[18391,2102,7],color=[CHAR,TEAL,AMBER])
ax.set_title("Most records in the 'Active' layer do not overlap the snapshot date"); ax.set_xlabel("Permit records")
for i,v in enumerate([18391,2102,7]): ax.text(v+200,i,str(v),va="center")
ax.set_xlim(0,21000); save(fig,"chart_snapshot_overlap.png")
# geography populated
fig,ax=plt.subplots(figsize=(8,4.0)); fields=["Onstreet","Council District","ZIP","Fromstreet","Tostreet"]; vals2=[6,6,6,20394,18917]
ax.barh(fields, vals2, color=TEAL)
for i,v in enumerate(vals2): ax.text(v+300,i,f"{v} of 20,500",va="center",fontsize=9)
ax.set_xlim(0,23000); ax.set_title("The named geography fields are blank on the NDOT-era records"); ax.invert_yaxis(); save(fig,"chart_geography_fields.png")
