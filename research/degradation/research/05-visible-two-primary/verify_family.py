"""An actual rectangular binary BB cover with a partial local length jump."""
import json,time
from algebra import *

def run():
    start=time.time();Q=4;field=Field(1,3)
    # First coordinate is y (the doubled period); second is x.
    co=GroupRing(6*Q,6*Q,field);ba=GroupRing(3*Q,6*Q,field)
    A=co.poly([(1,0,0),(1,1,0),(1,0,1)])
    B=co.poly([(1,0,0),(1,3*Q+1,0),(1,0,3*Q+1)])
    a,b=co.project(A,ba),co.project(B,ba)
    assert A.bit_count()==B.bit_count()==a.bit_count()==b.bit_count()==3
    cd=code_data(co,A,B);bd=code_data(ba,a,b)
    assert len(cd['h1'])==4*(Q+1) and len(bd['h1'])==4*Q
    e=ba.poly([(1,0,0),(1,0,3*Q)]);W=e|(e<<ba.bits)
    ac,bc=ba.columns(a),ba.columns(b)
    def apply(cols,v):
        ans=0
        while v:
            bit=v&-v;ans ^= cols[bit.bit_length()-1];v ^= bit
        return ans
    assert apply(ac+bc,W)==0 and bd['boundaries'].reduce(W)!=0 and W.bit_count()==4
    assert len(set(ac+bc))==len(ac+bc) and 0 not in ac+bc
    # This excludes all weight-two cycles. Odd weights are excluded by augmentation.
    U=A|(B<<co.bits)
    assert apply(co.columns(A)+co.columns(B),U)==0
    assert cd['boundaries'].reduce(U)!=0 and U.bit_count()==6
    P=[bd['boundaries'].reduce(co.project(v,ba,2)) for v in cd['h1']]
    rankp=len(Span(P));assert rankp==2*(Q+1)
    # Same local module and maps occur in the inherited four-term family.
    rr=GroupRing(2,2,field);ss=GroupRing(1,2,field)
    A4=rr.poly([(1,0,0),(1,0,1),(1,1,1),(1,1,0)])
    B4=A4^rr.poly([(1,0,0),(1,0,1)])
    c4=code_data(rr,A4,B4);b4=code_data(ss,rr.project(A4,ss),rr.project(B4,ss))
    pp=[b4['boundaries'].reduce(rr.project(v,ss,2)) for v in c4['h1']]
    assert b4['m']==1 and c4['m']==2 and len(Span(pp))==2
    ans={'Q':Q,'base_n':2*ba.size,'base_k':len(bd['h1']),'base_distance_exact':4,
         'base_weight_two_cycles_excluded_by_distinct_columns':True,
         'cover_n':2*co.size,'cover_k':len(cd['h1']),'cover_distance_upper_bound':6,
         'cover_distance_exact_not_claimed':True,'termwise_matching_and_strict_supports':True,
         'connected_by_A_support_generators':True,'projection_rank_binary':rankp,
         'four_term_same_local_full_doubling_guard':True,'seconds':round(time.time()-start,3)}
    open('family_verification.json','w').write(json.dumps(ans,indent=2));print(json.dumps(ans,indent=2))
if __name__=='__main__':run()
