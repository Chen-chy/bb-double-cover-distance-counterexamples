from pathlib import Path
ROOT = Path(__file__).resolve().parent
import subprocess,json,sys
from algebra import *
exe=str(ROOT/'circuit_search')
def check(L,A,B,bound):
    return json.loads(subprocess.check_output([exe,str(L),*map(str,A),*map(str,B),str(bound)]))
def distance(L,A,B,start=2,stop=20):
    for w in range(start,stop+1,2):
        r=check(L,A,B,w)
        if r['found']:
            assert BB(L,poly(A),poly(B)).logical(poly(r['u'])|(poly(r['v'])<<L))
            return w,r
    return None,r
out=[]
for L in range(15,128,6):
    d,lo=distance(L,[0,1,5],[0,11,13],stop=6)
    dc,hi=distance(2*L,[0,1,L+5],[0,L+11,13],start=2,stop=14)
    r={'L':L,'A':[0,1,5],'B':[0,11,13], 'At':[0,1,L+5],'Bt':[0,L+11,13],
       'k':lo['k'],'d':d,'k2':hi['k'],'d2':dc,'witness2':[hi.get('u'),hi.get('v')]}
    out.append(r); print(json.dumps(r),flush=True)
open(ROOT/'template_results.json','w').write(json.dumps(out,indent=2)+'\n')
