"""Finite adversarial cross-checks of the power-cycle lifting lemma.
This supplements the symbolic proof. It is not a distance search.
"""
from pathlib import Path
from itertools import product
import random,json,sys
from finite_algebra import Group,Code,poly,support
ROOT=Path(__file__).parent

def power(G,p,n):
    r=1
    while n:
        if n&1:r=G.mul(r,p)
        p=G.mul(p,p);n>>=1
    return r

def run():
    rng=random.Random(9406);counts={};examples=[]
    def count(k):counts[k]=counts.get(k,0)+1
    shapes=[(3,1),(6,1),(9,1),(12,1),(15,1),(3,2),(6,2),(6,4),(12,2),(3,4),(9,2)]
    for l,m in shapes:
        G=Group(l,m)
        for _ in range(45):
            a=rng.randrange(3);b=rng.randrange(a+1);M,N=1<<a,1<<b;q=M//N
            ts=[(i,j)for i in range(l)for j in range(m)if (N*i)%l==0 and (N*j)%m==0]
            x,y=rng.sample([(i,j)for i in range(l)for j in range(m)if i or j],2)
            h,j=rng.choice(ts),rng.choice(ts)
            ae=[(0,0),x,y]
            be=[(0,0),((q*x[0]+h[0])%l,(q*x[1]+h[1])%m),((q*y[0]+j[0])%l,(q*y[1]+j[1])%m)]
            if len(set(be))!=3:continue
            A=G.from_coords(ae);B=G.from_coords(be)
            assert power(G,A,M)==power(G,B,N)
            C=Code(G,A,B)
            u,v=power(G,A,M-1),power(G,B,N-1);z=u|(v<<G.size)
            count('base_pairs_examined')
            if not C.logical(z):continue
            count('nontrivial_canonical_base_cycles')
            for direction in (0,1):
                H=Group(2*l,m)if direction==0 else Group(l,2*m)
                step=(l,0)if direction==0 else (0,m)
                deck=H.pos(*step)
                for sheets in product((0,1),repeat=4):
                    aa=[(0,0)]+[(x+step[0]*s,y+step[1]*s)for (x,y),s in zip(ae[1:],sheets[:2])]
                    bb=[(0,0)]+[(x+step[0]*s,y+step[1]*s)for (x,y),s in zip(be[1:],sheets[2:])]
                    Ap,Bp=H.from_coords(aa),H.from_coords(bb)
                    # Occasionally change the constant-term sheet too, to exercise full discrepancy.
                    if rng.randrange(4)==0:Bp=H.shift(Bp,*step)
                    up,vp=power(H,Ap,M-1),power(H,Bp,N-1)
                    PA,PB=power(H,Ap,M),power(H,Bp,N)
                    epsPA=PA^H.shift(PA,*step)
                    if PA==PB:
                        out=up|(vp<<H.size);branch='identical_powers'
                    elif PA^PB==epsPA:
                        out=H.shift(up,*step)|(vp<<H.size);branch='deck_associate_powers'
                    else:
                        out=(up^H.shift(up,*step))|((vp^H.shift(vp,*step))<<H.size);branch='surviving_transfer'
                    D=Code(H,Ap,Bp)
                    assert D.logical(out),(G,ae,be,a,b,direction,sheets,branch)
                    assert out.bit_count()<=2*(3**a+3**b)
                    count('cover_cases_checked');count(branch)
                    if len(examples)<12 and branch=='surviving_transfer':
                        examples.append({'base_periods':[l,m],'a':a,'b':b,'A':ae,'B':be,'direction':direction,'sheets':sheets,'k':C.k,'k2':D.k,'cover_witness_weight':out.bit_count()})
    result={'seed':9406,'classification':'finite cross-check of symbolic lemma, not exact distances','counts':counts,'examples':examples}
    (ROOT/'frobenius_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(counts,indent=2))
if __name__=='__main__':run()
