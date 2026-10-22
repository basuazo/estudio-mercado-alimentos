"""Compara series trimestrales de Google Trends (temas) entre Australia y Chile.

Uso: python scripts/analizar_australia_vs_chile.py <trimestral.csv> <salida_resumen.csv> <salida_correlacion.csv>
Despegue = primer trimestre en que la media movil de 4 trimestres supera el 25 % de su maximo y se mantiene 3 trimestres.
Rezago = despegue Chile - despegue Australia (trimestres). Correlacion = crecimiento anual de la media movil, con rezagos de 0 a 12 trimestres.
Tramos de 6+ trimestres en cero entre 2016T3 y 2020T1 se tratan como falla de datos de Trends y se interpolan.
"""
import pandas as pd, numpy as np
import sys
f, salida_resumen, salida_corr = sys.argv[1:4]
d=pd.read_csv(f); q=[c for c in d.columns[3:]]
def clean(v):
    v=v.astype(float).copy()
    # artefacto de Trends: tramo de >=6 trimestres en cero entre 2016Q3 y 2020Q1 con datos antes y despues
    z=(v==0); idx=list(v.index)
    i=0
    while i<len(v):
        if z.iloc[i]:
            j=i
            while j<len(v) and z.iloc[j]: j+=1
            if j-i>=6 and i>0 and j<len(v) and v.iloc[i-1]>=3 and v.iloc[j]>=3 and idx[i]>='2016Q3' and idx[j-1]<='2020Q1':
                v.iloc[i:j]=np.nan
            i=j
        else: i+=1
    return v.interpolate(limit_area='inside')
rows=[];xc=[]
for c,g in d.groupby('concepto',sort=False):
    s={p:clean(g[g.pais==p][q].iloc[0].rename(index=lambda x:x)) for p in ['AU','CL']}
    s={p:pd.Series(v.values,index=pd.PeriodIndex(q,freq='Q')) for p,v in s.items()}
    ma={p:v.rolling(4,min_periods=4).mean() for p,v in s.items()}
    r={'concepto':c}
    for p in ['AU','CL']:
        m=ma[p]; mx=m.max(); r[f'max_media_movil_{p}']=round(mx,1)
        ab=(m>=0.25*mx)
        t=None
        for k in range(len(m)-2):
            if ab.iloc[k] and ab.iloc[k+1] and ab.iloc[k+2]: t=m.index[k]; break
        r[f'despegue_{p}']=str(t) if t is not None else ''
        r[f'peak_{p}']=str(m.idxmax())
        r[f'nivel_actual_vs_peak_{p}_pct']=round(100*m.iloc[-1]/mx)
    r['rezago_trimestres']=(pd.Period(r['despegue_CL'],'Q')-pd.Period(r['despegue_AU'],'Q')).n if r['despegue_AU'] and r['despegue_CL'] else ''
    ga=np.log(ma['AU']+1).diff(4); gc=np.log(ma['CL']+1).diff(4)
    best=(None,-9)
    for L in range(0,13):
        x=pd.concat([ga.shift(L),gc],axis=1).dropna(); x=x[x.index>=pd.Period('2012Q1','Q')]
        if len(x)<16: continue
        cc=x.corr().iloc[0,1]; xc.append({'concepto':c,'rezago_trimestres':L,'correlacion':round(cc,2),'n_trimestres':len(x)})
        if cc>best[1]: best=(L,cc)
    r['corr_crecimiento_sin_rezago']=next((z['correlacion'] for z in xc if z['concepto']==c and z['rezago_trimestres']==0),'')
    r['mejor_rezago_corr_trim']=best[0]; r['corr_mejor_rezago']=round(best[1],2)
    rows.append(r)
o=pd.DataFrame(rows)
def tipo(r):
    if r['max_media_movil_CL']<20: return 'no despego en Chile'
    L=r['rezago_trimestres']
    if L=='' : return 'sin dato'
    if L>=2: return 'Australia primero'
    if L<=-2: return 'Chile primero'
    return 'casi simultaneo'
o['patron']=o.apply(tipo,axis=1)
o.to_csv(salida_resumen,index=False)
pd.DataFrame(xc).to_csv(salida_corr,index=False)
pd.set_option('display.width',260)
print(o[['concepto','despegue_AU','despegue_CL','rezago_trimestres','patron','peak_AU','peak_CL','nivel_actual_vs_peak_AU_pct','nivel_actual_vs_peak_CL_pct','max_media_movil_CL','corr_crecimiento_sin_rezago','mejor_rezago_corr_trim','corr_mejor_rezago']].to_string())
print(o.patron.value_counts())
lag=pd.to_numeric(o[o.patron.isin(['Australia primero','casi simultaneo','Chile primero'])].rezago_trimestres)
print('mediana rezago trimestres',lag.median(), 'media',lag.mean())
X=pd.DataFrame(xc); print(X.groupby('rezago_trimestres').correlacion.median())
