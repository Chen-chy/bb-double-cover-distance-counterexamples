"""Independent verifier of the saved primal/dual finite certificates.

Does not import the construction, field, rank, or span implementations.
Every non-boundary is certified by a functional orthogonal to every boundary
and having value one on the proposed cycle.
"""
from pathlib import Path
import json


def support(v):
    return [i for i in range(v.bit_length()) if (v >> i) & 1]


def translate(indices,x,y,L,M):
    return {(((i//M+x)%L)*M+(i%M+y)%M) for i in indices}


def check(L,M,A,B,z,phi):
    N=L*M;mask=(1<<N)-1
    assert len(A)==len(set(A))==3 and len(B)==len(set(B))==3
    u=support(z&mask);v=support(z>>N)
    checks=set()
    for inds,P in [(u,A),(v,B)]:
        for i in inds:
            s=translate(P,i//M,i%M,L,M)
            checks.symmetric_difference_update(s)
    assert not checks
    U=set(support(phi&mask));V=set(support(phi>>N))
    for i in range(N):
        left=translate(B,i//M,i%M,L,M)
        right=translate(A,i//M,i%M,L,M)
        assert (len(left&U)+len(right&V))%2==0
    assert (len(set(u)&U)+len(set(v)&V))%2==1


def main():
    here=Path(__file__).parent
    rows=json.loads((here/'finite_cover_certificates.json').read_text())
    for row in rows:
        L,M=row['periods'];direction=row['doubling_direction']
        check(L,M,row['A'],row['B'],int(row['base_cycle'],16),int(row['base_dual'],16))
        LL=L*(2 if direction==0 else 1);MM=M*(2 if direction==1 else 1)
        for base,cover in [(row['A'],row['cover_A']),(row['B'],row['cover_B'])]:
            projected={((i//MM)%L)*M+(i%MM)%M for i in cover}
            assert projected==set(base)
        check(LL,MM,row['cover_A'],row['cover_B'],int(row['cover_cycle'],16),int(row['cover_dual'],16))
        assert int(row['cover_cycle'],16).bit_count()==row['cover_witness_weight']<=row['symbolic_bound']
    out={'independently_audited_pairs':len(rows),'primal_dual_certificates':2*len(rows),
         'all_cycles_nonboundaries_and_term_matched_covers_verified':True,
         'distance_lower_bounds_claimed':False}
    (here/'finite_certificate_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
