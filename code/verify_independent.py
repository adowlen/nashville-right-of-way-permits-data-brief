import pandas as pd, json, os
HERE=os.path.dirname(__file__); ROOT=os.path.normpath(os.path.join(HERE,"..")); DATA=os.path.join(ROOT,"data")
df=pd.read_csv(os.path.join(DATA,"nashville_row_raw.csv"), low_memory=False)
stats=json.load(open(os.path.join(ROOT,"stats.json")))
checks={}
checks["rows"]= (len(df)==20500)
for c in ['Scheduled__Start','Scheduled__End']:
    df[c]=pd.to_datetime(df[c], unit='ms', utc=True)
df['dur']=(df['Scheduled__End']-df['Scheduled__Start']).dt.total_seconds()/86400
checks["excavation_n"]= int((df['Permit__Type'].str.contains('Excavation',na=False)).sum())==6348
exc=df[df['Permit__Type'].str.contains('Excavation',na=False)]
checks["excavation_days_share"]= bool(abs(exc.loc[exc['dur']>=0,'dur'].sum()/df.loc[df['dur']>=0,'dur'].sum()*100-80.6)<0.15)
snap=pd.Timestamp('2026-11-12',tz='UTC')
checks["overlap"]= int(((df['Scheduled__Start']<=snap)&(df['Scheduled__End']>=snap)).sum())==2102
checks["onstreet_populated"]= int(df['Onstreet'].notna().sum())==6
checks["ervin_n"]= int((df['Company']=='ERVIN CABLE CONSTRUCTION LLC').sum())==5893
checks["negative_n"]= int((df['dur']<0).sum())==17
checks["median_nonneg"]= float(df.loc[df['dur']>=0,'dur'].median())==13.0
out={"checks":{k:bool(v) for k,v in checks.items()},"all_pass":bool(all(checks.values()))}
json.dump(out, open(os.path.join(DATA,"verify_independent_output.json"),"w"), indent=2)
print(out); assert out["all_pass"]
