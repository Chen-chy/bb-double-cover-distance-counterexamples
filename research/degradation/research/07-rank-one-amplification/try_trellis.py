from core import *
import subprocess,json

def run(cols,labels,c,potential=None):
 cols,labels=reduce_generator(cols,labels,c)
 ds=[max(map(deg,v)) for v in cols]
 data=f'{len(cols)} {len(cols[0])} {deg(c)} {c}\n'
 for v,d,l in zip(cols,ds,labels):data+=f'{d} {l} '+ ' '.join(map(str,v))+'\n'
 p=subprocess.run(['./trellis']+([potential] if potential else []),input=data,text=True,capture_output=True,timeout=120)
 if p.returncode:raise Exception((data,p.stdout,p.stderr))
 lines=p.stdout.splitlines();distance=int(lines[0].split()[1]);bits=list(map(int,lines[1][7:].strip(',').split(',')))
 fs=[sum(1<<i for i,b in enumerate(bits) if b>>j&1) for j in range(len(cols))]
 Y=[0]*len(cols[0]);label=0
 for f,v,l in zip(fs,cols,labels):
  for i,x in enumerate(v):Y[i]^=mul(f,x)
  label^=mod(mul(f,l),c)
 assert weights(Y)==distance and label
 return dict(distance=distance, degrees=ds, modulus=c, potential=potential, trellis=lines[0], input_exponents=[supp(f) for f in fs],generator=[[supp(x)for x in v]for v in cols],labels=labels,physical=[supp(x)for x in Y])

if __name__=='__main__':
 out=[];A=poly(0,1,2)
 for eb in [(2,7),(8,7),(8,13)]:
  B=poly(0,*eb);c=gcd(A,B)
  base=run([[exact(B,c),exact(A,c)]],[1],c)
  cols,delta=cover_generator(A,B)
  cov=run(cols,[1,0],c)
  row=dict(A=supp(A),B=supp(B),c=supp(c),base=base,cover=cov,ratio=cov['distance']/base['distance'])
  out.append(row);print(eb,base['distance'],cov['distance'],flush=True)
  json.dump(out,open('trellis_results.json','w'),indent=2)
