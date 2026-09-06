"""Construct optimized compact-generator images in actual bivariate covers.
The binary linear-algebra routines are retained from the supplied prior bundle;
a separate auditor checks all primal/dual outputs without those routines.
No finite quantum minimum distances are inferred from these witnesses.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json,random
from finite_arithmetic import Group,Code,bits,subgroup,odd_part

def two_part(G,g):return G.add(g,G.scale(odd_part(G,g),-1))

def sharp(G,A,B,q,h,k,shape=None):
    T=subgroup(G,[h,k]);O=subgroup(G,[odd_part(G,h),odd_part(G,k)])
    h2,k2=two_part(G,h),two_part(G,k)
    if shape is None:
        M=max(G.order(h2),G.order(k2));m=len(T)//len(O)//M
        maxgen=h2 if G.order(h2)==M else k2
    else:
        M,m,maxgen=shape
    e=G.poly(O)
    # For collapsed torsion, use the full universal norm sum, including repeats.
    N=G.poly(G.scale(maxgen,m*j) for j in range(M//m))
    EN=G.mul(e,N)
    u=G.mul(EN,G.power(A,q*m-1));v=G.mul(EN,G.power(B,m-1))
    predicted=len(O)*(M//m)*3**(m.bit_length()-1)*(3**(q.bit_length()-1)+1)
    return u|(v<<G.n),dict(M=M,m=m,odd_size=len(O),universal_weight=predicted,
                           image_torsion_size=len(T),max_generator=list(G.coords(maxgen)))

def mkrecord(G,H,A,B,AA,BB,q,h,k,hh,kk,z,w,baseinfo,coverinfo,kind,metadata=None):
    base,cover=Code(G,A,B),Code(H,AA,BB)
    p1=base.certificate(z)
    if p1 is None:return None
    p2=cover.certificate(w)
    assert p2 is not None,('FAILED_SURVIVAL',G.L,G.M,q,h,k,baseinfo,coverinfo)
    assert z.bit_count()<=baseinfo['universal_weight']
    assert w.bit_count()<=coverinfo['universal_weight']
    ratio=coverinfo['universal_weight']/baseinfo['universal_weight']
    assert ratio in (1,1.5,2),(baseinfo,coverinfo)
    return dict(periods=[G.L,G.M],cover_periods=[H.L,H.M],q=q,
        A=list(bits(A)),B=list(bits(B)),cover_A=list(bits(AA)),cover_B=list(bits(BB)),
        base_k=base.k,cover_k=cover.k,base_cycle=hex(z),cover_cycle=hex(w),
        base_h=list(G.coords(h)),base_k_torsion=list(G.coords(k)),
        cover_h=list(H.coords(hh)),cover_k_torsion=list(H.coords(kk)),
        base_dual=hex(p1),cover_dual=hex(p2),base_cycle_weight=z.bit_count(),
        cover_cycle_weight=w.bit_count(),base_compact_data=baseinfo,
        cover_compact_data=coverinfo,compact_ratio=ratio,kind=kind,
        metadata=metadata or {})

def ordinary(G,q,h,k,mask,direction):
    X,Y=G.pos(1,0),G.pos(0,1)
    ap=[0,X,Y];bp=[0,G.add(h,G.scale(X,q)),G.add(k,G.scale(Y,q))]
    A,B=G.poly(ap),G.poly(bp)
    if A.bit_count()!=3 or B.bit_count()!=3:return None
    z,bi=sharp(G,A,B,q,h,k)
    if Code(G,A,B).certificate(z) is None:return None
    H=Group(G.L*(2 if direction==0 else 1),G.M*(2 if direction==1 else 1))
    deck=H.pos(G.L,0) if direction==0 else H.pos(0,G.M)
    def lift(p,bit):
        v=H.pos(*G.coords(p))
        return H.add(v,deck) if mask>>bit&1 else v
    Xp,Yp=lift(X,0),lift(Y,1)
    pB,qB=lift(bp[1],2),lift(bp[2],3)
    AA,BB=H.poly([0,Xp,Yp]),H.poly([0,pB,qB])
    hh=H.add(pB,H.scale(Xp,-q));kk=H.add(qB,H.scale(Yp,-q))
    w,ci=sharp(H,AA,BB,q,hh,kk)
    J=subgroup(H,[hh,kk]);kind='connected' if deck in J else 'split_components'
    return mkrecord(G,H,A,B,AA,BB,q,h,k,hh,kk,z,w,bi,ci,kind,
                    {'mask':mask,'direction':direction})

def collapsed_examples():
    rows=[]
    # Universal T=C_2 x C_2 -> T'=C_4 x C_2, but the second generator
    # is sent to the identity in both finite groups; deck remains nonidentity.
    for L in (6,18,30):
        G=Group(L,3);H=Group(2*L,3)
        h=G.pos(L//2,0);hh=H.pos(L//2,0)
        for q in (1,2,4):
            A=G.poly([0,G.pos(1,0),G.pos(0,1)])
            B=G.poly([0,G.add(h,G.pos(q,0)),G.add(h,G.pos(0,q))])
            AA=H.poly([0,H.pos(1,0),H.pos(0,1)])
            BB=H.poly([0,H.add(hh,H.pos(q,0)),H.add(hh,H.pos(0,q))])
            z,bi=sharp(G,A,B,q,h,h,shape=(2,2,h))
            w,ci=sharp(H,AA,BB,q,hh,hh,shape=(4,2,hh))
            row=mkrecord(G,H,A,B,AA,BB,q,h,h,hh,hh,z,w,bi,ci,'torsion_collapse',
                         {'universal_base_2_group':[2,2],
                          'universal_cover_2_group':[4,2],
                          'collapsed_generator':'w maps to identity',
                          'deck_image':list(H.coords(H.scale(hh,2)))})
            if row:rows.append(row)
    return rows

def main():
    rng=random.Random(202609060404);rows=[];tested=0
    for L,N in [(3,3),(6,3),(3,6),(6,6),(12,3),(12,6),(6,12),(9,6),(12,9),(15,6)]:
        G=Group(L,N)
        choices={0}
        for divisor in (2,3,4):
            if L%divisor==0:choices.add(G.pos(L//divisor,0))
            if N%divisor==0:choices.add(G.pos(0,N//divisor))
        pairs=list(product(sorted(choices),repeat=2));rng.shuffle(pairs)
        for h,k in pairs[:8]:
            for q in (1,2,4):
                for mask in (0,1,4,5,10,15):
                    for direction in (0,1):
                        tested+=1
                        row=ordinary(G,q,h,k,mask,direction)
                        if row:rows.append(row)
    rows+=collapsed_examples()
    assert any(r['compact_ratio']==1.5 for r in rows)
    assert any(r['kind']=='torsion_collapse' for r in rows)
    counts={str(r):sum(x['compact_ratio']==r for x in rows) for r in (1,1.5,2)}
    result=dict(parameter_checks=tested,certified_pairs=len(rows),compact_ratio_counts=counts,
                even_coordinate_covers=sum(r['periods'][0 if r['cover_periods'][0]>r['periods'][0] else 1]%2==0 for r in rows),
                odd_norm_cases=sum(r['base_compact_data']['odd_size']>1 for r in rows),
                explicit_torsion_collapse_cases=sum(r['kind']=='torsion_collapse' for r in rows),
                caveat='Exact finite logical certificates. Compact weights are symbolic universal weights; finite quantum distances are not claimed.')
    here=Path(__file__).parent
    (here/'finite_replacement_certificates.json').write_text(json.dumps(rows,indent=2)+'\n')
    (here/'finite_replacement_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
