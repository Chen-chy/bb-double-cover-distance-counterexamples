"""Finite checks for the symbolic sharpness family L>=9 odd, 3|L."""
from pathlib import Path
import json
from arithmetic import *
ROOT=Path(__file__).parent

def main():
    A=poly([0,1,2]);records=[];certs=[]
    for L in (9,15,21):
        D=data(A,A,0,L,0);C=Cover(L,0,A,A,0)
        assert D['c']==D['G']==D['g0']==D['H']==A
        assert D['E']==1 and C.k==4
        assert len(set(C.columns))==4*L
        # No odd-weight cycle since each column has odd weight; no
        # weight-two cycle since every column is distinct.
        assert all(x.bit_count()==3 for x in C.columns)
        z=C.encode_epsilon(set(),set(),{0},{0})
        assert z.bit_count()==4 and C.logical(z)
        baseboundaries=Span()
        def rot(x,i):return ((x<<i)&((1<<L)-1))|(x>>(L-i)) if i else x
        for i in range(L):
            a=rot(A,i);baseboundaries.add(a|(a<<L))
        basez=1|(1<<L)
        assert not baseboundaries.contains(basez)
        assert 2*(L-len(baseboundaries))==4
        records.append({'L':L,'base_parameters':[2*L,4,2],'cover_parameters':[4*L,4,4],
                        'classification':'exact finite cross-check of the uniform symbolic family'})
        certs.append(C.certificate(z,{'source':'one_sided_sharpness','base_A':[0,1,2],'base_B':[0,1,2],'delta':0}))
    (ROOT/'sharpness_summary.json').write_text(json.dumps(records,indent=2)+'\n')
    (ROOT/'sharpness_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
    print(json.dumps(records,indent=2))
if __name__=='__main__':main()
