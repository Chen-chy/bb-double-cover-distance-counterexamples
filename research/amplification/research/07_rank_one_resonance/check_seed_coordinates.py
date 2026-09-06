"""Exact algebraic check of the supplied 7/3 strip in the new resonant form.
No distance search or new exact-distance claim is made by this script.
"""
from pathlib import Path
import json
from arithmetic import *
ROOT=Path(__file__).parent
A={0,-1,4};B={0,-13,-2};L=39
D=ldata(A,B,1,L,0)
assert D['c']==poly([0,1,5])
assert D['E']==poly([0,1,2])
assert D['H']==D['g0']==D['E']
# Base logical in the supplied unnormalized strip: (U,V).
U={0,1,5,10};V={0,2}
u=ls(U,1);v=ls(V,13)
f=ls(v,1) # a=z^-1, so f=zv
assert lm(D['b'],f)==u and lm(D['a'],f)==v
assert len(u)+len(v)==6
assert lmod(f,D['g0'])!=0
# A known cover cycle from the supplied strip, gauged to the minority-constant form.
U0={1,4,6,8,10,11};U1={0,3,7,8,9};V0=set();V1={0,2,3}
parts=(ls(U0,1),ls(U1,1),ls(V0,13),ls(V1,13))
assert universal_lcycle(A,B,1,parts)
C=LaurentCover(L,0,A,B,1)
z=C.encode_physical(parts)
assert C.logical(z) and z.bit_count()==14 and C.k==4
transfer=C.encode_epsilon(set(),set(),u,v)
assert C.cycle(transfer) and C.bd.contains(transfer)
result={'A':sorted(A),'B':sorted(B),'c':terms(D['c']),'E':terms(D['E']),
        'g0':terms(D['g0']),'H':terms(D['H']),'R':-6,'S':-3,'g':3,'p':-2,'q':-1,
        'base_witness_weight':6,'cover_witness_weight':14,'cover_k':4,
        'base_compact_transfer_is_boundary':True,
        'scope':'new coordinate and nonboundary check; exact distances 6 and 14 are inherited from the supplied certificate'}
(ROOT/'seed_coordinate_check.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'seed_nonboundary_certificate.json').write_text(json.dumps(C.certificate(z,{'source':'supplied_seed','base_A':sorted(A),'base_B':sorted(B),'delta':1}),indent=2)+'\n')
print(json.dumps(result,indent=2))
