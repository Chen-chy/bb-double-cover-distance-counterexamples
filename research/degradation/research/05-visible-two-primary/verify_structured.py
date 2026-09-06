"""Structured high-contact and cyclic-Sylow matrix checks."""
import json,time,random
from algebra import *
from verify_local import parity_rank

def powf(field,a,n):
    v=1
    while n:
        if n&1:v=field.mul(v,a)
        a=field.mul(a,a);n//=2
    return v

def check_pair(r,A,B):
    base=GroupRing(r.M//2,r.N,r.field);deg=r.field.degree
    co=code_data(r,A,B);ba=code_data(base,r.project(A,base),r.project(B,base))
    m2,m=co['m'],ba['m']
    assert m<=m2<=2*m and m.bit_count()<=2 and m2.bit_count()<=2
    if m2>m:assert m.bit_count()==1 and (m2-m).bit_count()==1
    assert loewy_profile(r,co['h0'],co['check'],1)==[deg*j for j in range(m2,-1,-1)]
    assert loewy_profile(r,co['h1'],co['boundaries'],2)==[2*deg*j for j in range(m2,-1,-1)]
    pp=[ba['boundaries'].reduce(r.project(v,base,2)) for v in co['h1']]
    assert len(Span(pp))==deg*m2
    kk=[]
    for vv in kernel(pp):
        z=0
        for i,h in enumerate(co['h1']):
            if (vv>>i)&1:z ^= h
        kk.append(z)
    profile=loewy_profile(r,kk,co['boundaries'],2)
    assert profile==[deg*(max(m-j,0)+max(m2-m-j,0)) for j in range(m+1)]
    return {'M':r.M,'N':r.N,'m':m,'m2':m2,'projection_rank_over_field':len(Span(pp))//deg,'kernel_profile_over_field':[n//deg for n in profile]}

def run():
    start=time.time();field=Field(2,7);rows=[]
    for r in range(1,4):
      for s in range(4-r):
        Q=1<<r;S=1<<s;M=2*Q*S
        ring=GroupRing(M,M,field)
        A=ring.poly([(1,0,0),(2,1,0),(3,0,1)])
        ps=[(3*Q+1,0),(0,3*Q+1)] if r%2==0 else [(1,3*Q),(3*Q,1)]
        B=ring.poly([(1,0,0)]+[(powf(field,2,(a+2*b)*S),a*S,b*S) for a,b in ps])
        ans=check_pair(ring,A,B)
        assert ans['m']==Q*S and ans['m2']==S*(Q+1)
        ans.update(r=r,s=s);rows.append(ans)
    rng=random.Random(622967);cyclic=0
    for M in (2,4,8,16,32,64):
      for _ in range(12):
        ring=GroupRing(M,1,field)
        while True:
            ps=[(rng.randrange(M),0) for _ in range(4)]
            if parity_rank(ps,M,1)==1:break
        A=ring.poly([(1,0,0),(2,*ps[0]),(3,*ps[1])])
        B=ring.poly([(1,0,0),(2,*ps[2]),(3,*ps[3])])
        ans=check_pair(ring,A,B);assert ans['m']==ans['m2']==1;cyclic+=1
    out={'partial_growth_cases':rows,'cyclic_sylow_cases':cyclic,'all_checks_pass':True,'seconds':round(time.time()-start,3)}
    open('structured_verification.json','w').write(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':run()
