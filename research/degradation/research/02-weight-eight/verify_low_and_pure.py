"""Independent integer-minor audit of all finite/strip and pure certificates.
No floating point and no Smith/Hermite implementation is used for the
low-free-rank audit. Original five relation rows are reconstructed anew.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,math,hashlib
from certificate_common import reconstruct,reducer,poly,A,Z,add
ROOT=Path(__file__).resolve().parent

def det3(rows,cols):
 a,b,c=rows;i,j,k=cols
 return a[i]*(b[j]*c[k]-b[k]*c[j])-a[j]*(b[i]*c[k]-b[k]*c[i])+a[k]*(b[i]*c[j]-b[j]*c[i])
def det4(rows):
 return sum((-1)**j*rows[0][j]*det3(rows[1:],[i for i in range(4)if i!=j])for j in range(4))
def index3(rows):return math.gcd(*(abs(det3([rows[i]for i in iset],jset))for iset in combinations(range(len(rows)),3)for jset in combinations(range(4),3)))
def index2(rows):return math.gcd(*(abs(rows[i][a]*rows[j][b]-rows[i][b]*rows[j][a])for i,j in combinations(range(len(rows)),2)for a,b in combinations(range(4),2)))
counts=Counter();maximum={0:0,1:0};seen=set();max_ids={0:[],1:[]}
lines=(ROOT/'low_free_lattices.tsv').read_text().splitlines()
for li,line in enumerate(lines):
 r,fr,tor,bound,mat,src=line.split('\t');r,fr,tor,bound=map(int,(r,fr,tor,bound));src=list(map(int,src.split(',')))
 assert mat not in seen;seen.add(mat);assert src[1].bit_count()==8-r
 a=list(map(int,mat.strip(',').split(',')));rr=[tuple(a[i:i+4])for i in range(0,16,4)];norm=reducer(rr)
 assert sum(any(v)for v in rr)==4-fr
 orig,_=reconstruct(src);assert all(norm(row)==Z for row in orig)
 if fr==0:
  assert abs(det4(rr))==tor
  idx=math.gcd(*(abs(det4([orig[i]for i in inds]))for inds in combinations(range(5),4)))
  assert idx==tor and bound==tor
 else:
  assert fr==1 and index3(rr)==index3(orig)==tor
  c=[(-1)**j*det3(rr[:3],[i for i in range(4)if i!=j])for j in range(4)]
  assert math.gcd(*c)==tor
  v=[x//tor for x in c]
  assert math.gcd(*v)==1 and all(sum(x*y for x,y in zip(row,v))==0 for row in orig)
  R=max(max(0,v[0],v[1])-min(0,v[0],v[1]),max(0,v[2],v[3])-min(0,v[2],v[3]))
  assert bound==4*tor*R
 counts[fr]+=1
 if bound>maximum[fr]:maximum[fr]=bound;max_ids[fr]=[li]
 elif bound==maximum[fr]:max_ids[fr].append(li)
result={'checked_lattices':len(lines),'free_rank_counts':dict(counts),'maximum_finite_order':maximum[0],'maximum_strip_bound':maximum[1],'maximizer_row_ids':max_ids,'input_sha256':hashlib.sha256((ROOT/'low_free_lattices.tsv').read_bytes()).hexdigest()}
(ROOT/'low_free_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

pure=[]
for li,line in enumerate((ROOT/'pure_eight.tsv').read_text().splitlines()):
 r,fr,tor,mat,wit,src=line.split('\t');r,fr,tor=map(int,(r,fr,tor));src=list(map(int,src.split(',')))
 a=list(map(int,mat.strip(',').split(',')));rr=[tuple(a[i:i+4])for i in range(0,16,4)];norm=reducer(rr)
 assert r==8 and fr==0 and sum(any(row)for row in rr)==2
 orig,origw=reconstruct(src);assert all(norm(row)==Z for row in orig)
 assert index2(orig)==index2(rr)==tor
 assert all(row[2:]==(0,0)for row in rr)
 W={(int(t[0]),tuple(map(int,t[1:])))for t in [u.strip(',').split(',')for u in wit.strip(';').split(';')]}
 assert len(W)==8 and all(b==0 for b,q in W)
 ow={(b,norm(q))for b,q in origw};assert len(ow)==8
 assert sorted(W)==min(sorted((b,norm(tuple(x-y for x,y in zip(q,t))))for b,q in ow)for _,t in ow)
 assert len(poly(A,norm))==3 and not poly([add(q,t)for b,q in W for t in A],norm)
 first=math.gcd(*(x for row in rr for x in row));second=tor//first
 pure.append({'id':li,'group_order':tor,'invariant_factors':[v for v in (first,second)if v!=1]})
result={'checked_pure_presentations':len(pure),'maximum_group_order':max(x['group_order']for x in pure),'group_types':sorted(set(tuple(x['invariant_factors'])for x in pure)),'certificates':pure,'input_sha256':hashlib.sha256((ROOT/'pure_eight.tsv').read_bytes()).hexdigest()}
(ROOT/'pure_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
