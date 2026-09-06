"""Generate block-colouring orbit representatives for the eight-vertex graphs."""
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
out=[];counts=Counter()
for line in (ROOT/'graph_auts_8.txt').read_text().splitlines():
 x=list(map(int,line.split()));gi,na=x[:2];auts=[x[i:i+8]for i in range(2,len(x),8)];assert len(auts)==na
 for r in range(4,8):
  seen=set()
  for mask in range(256):
   if mask.bit_count()!=8-r or mask in seen:continue
   orbit={sum(((mask>>j)&1)<<a[j]for j in range(8))for a in auts}
   if r==4:orbit|={255^m for m in orbit}
   seen|=orbit;out.append((gi,r,mask));counts[r]+=1
(ROOT/'colorings_8.txt').write_text(''.join(f'{g} {r} {m}\n'for g,r,m in out))
assert len(out)==877
print('Colouring orbit counts:',dict(counts))
