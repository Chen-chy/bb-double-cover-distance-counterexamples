"""A compact weight-eight testbed, without an exact-distance claim."""
from pathlib import Path
import json
from verify_finite_covers import Group,Code


def main():
    records=[]
    for L in (9,15,21):
        G=Group(2*L,L);H=Group(4*L,L)
        A=G.poly([0,G.pos(1,0),G.pos(0,1)])
        B=G.poly([0,G.pos(L+2,0),G.pos(L,2)])
        eta=G.poly([0,G.pos(L,0)])
        u=G.mul(eta,A);v=eta;z=u|(v<<G.n)
        C=Code(G,A,B);phi=C.certificate(z)
        assert phi is not None and z.bit_count()==8
        AA=H.poly([0,H.pos(1,0),H.pos(0,1)])
        BB=H.poly([0,H.pos(L+2,0),H.pos(L,2)])
        norm=H.poly([H.pos(j*L,0) for j in range(4)])
        UU=H.mul(norm,AA);VV=norm;zz=UU|(VV<<H.n)
        CC=Code(H,AA,BB);psi=CC.certificate(zz)
        assert psi is not None and zz.bit_count()==16
        records.append({'L':L,'base_k':C.k,'cover_k':CC.k,
                        'base_logical_weight':8,'cover_logical_weight':16,
                        'exact_minimum_distances_not_claimed':True,
                        'base_cycle':hex(z),'base_dual':hex(phi),
                        'cover_cycle':hex(zz),'cover_dual':hex(psi)})
    out={'universal_presentation':'Z^2 x C_2; A=1+x+y; B=1+h*x^2+h*y^2',
         'universal_compact_generator':'((1+h)A,1+h)',
         'cases':records}
    Path(__file__).with_name('weight8_testbed.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'cases':[{k:r[k] for k in ('L','base_k','cover_k','base_logical_weight','cover_logical_weight')} for r in records]},indent=2))

if __name__=='__main__':main()
