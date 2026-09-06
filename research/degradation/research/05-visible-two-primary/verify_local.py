"""Direct matrices test the local theorem; no contact formula enters the matrices."""
import json,random,time
from collections import Counter
from algebra import Field,GroupRing,Span,kernel,quotient_basis,code_data,loewy_profile

def parity_rank(points,M,N):
    active=[i for i,L in enumerate((M,N)) if L>1]
    rows=[sum(((v[i]&1)<<j) for j,i in enumerate(active)) for v in points]
    return len(Span(rows))

def run():
    start=time.time();rng=random.Random(260906);out=[];hist=Counter()
    specs=[(2,2),(4,2),(4,4),(8,4),(8,8),(16,8)]
    for field in (Field(2,7),Field(3,11)):
      for M,N in specs:
       for trial in range(32):
        ring=GroupRing(M,N,field);base=GroupRing(M//2,N,field)
        while True:
         ps=[(rng.randrange(M),rng.randrange(N)) for _ in range(4)]
         if parity_rank(ps,M,N)==2:break
        alpha=rng.randrange(2,1<<field.degree);gamma=rng.randrange(2,1<<field.degree)
        A=ring.poly([(1,0,0),(alpha,*ps[0]),(alpha^1,*ps[1])])
        B=ring.poly([(1,0,0),(gamma,*ps[2]),(gamma^1,*ps[3])])
        a=ring.project(A,base);b=ring.project(B,base)
        co=code_data(ring,A,B);ba=code_data(base,a,b)
        m2,m=co['m'],ba['m'];deg=field.degree
        assert m and m2 and m.bit_count()<=2 and m2.bit_count()<=2,(M,N,ps,m,m2)
        assert m<=m2<=2*m
        if m2>m:
         assert m.bit_count()==1 and (m2-m).bit_count()==1
        hist[(m,m2)]+=1
        p0=loewy_profile(ring,co['h0'],co['check'],1)
        p1=loewy_profile(ring,co['h1'],co['boundaries'],2)
        assert p0==[deg*j for j in range(m2,-1,-1)]
        assert p1==[2*deg*j for j in range(m2,-1,-1)]
        projected=[ba['boundaries'].reduce(ring.project(v,base,2)) for v in co['h1']]
        assert len(Span(projected))==deg*m2
        ker_coordinates=kernel(projected)
        ker=[]
        for v in ker_coordinates:
          x=0
          while v:
           b0=v&-v;x^=co['h1'][b0.bit_length()-1];v^=b0
          ker.append(x)
        kp=loewy_profile(ring,ker,co['boundaries'],2)
        expected=[deg*(max(m-j,0)+max(m2-m-j,0)) for j in range(m+1)]
        assert kp==expected,(kp,expected)
        # Independent invariant of the image, also forced by the two branch form.
        im=Span(projected).vectors()
        ip=loewy_profile(base,im,ba['boundaries'],2)
        assert ip==expected,(ip,expected)
        out.append({'degree':deg,'M':M,'N':N,'alpha':alpha,'gamma':gamma,'points':ps,'m':m,'m2':m2})
    result={'random_exact_cases':len(out),'local_length_histogram':{f'{m}->{m2}':n for (m,m2),n in sorted(hist.items())},
      'checked':['curvilinear H0','H1 free rank two over H0 by radical profiles',
                 'two-bit local lengths','doubling length rule','projection rank',
                 'kernel and image radical profiles of the projection normal form'],
      'seconds':round(time.time()-start,3)}
    open('local_cases.json','w').write(json.dumps(out,indent=2))
    open('local_verification.json','w').write(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
if __name__=='__main__':run()
