#!/usr/bin/env python3
"""Check the necessary active-odd-summand qualification.
The inherited family has a weight-six boundary, not a logical, in its norm sector.
This script does not certify its minimum distance.
"""
from pathlib import Path
import json
from verify_twists import Ring

def main():
    cases=[]
    for L in (4,16,64):
        R=Ring((3*L,3*L));z=R.zero;x=(1,0);y=(0,1);t=(L,0)
        A={z,x,y};B={z,R.add(t,x),R.add(R.scale(t,2),y)}
        E={z,t,R.scale(t,2)}
        assert R.mul(E,A)==R.mul(E,B)
        assert R.mul(R.power(A,L),E)==R.mul({R.scale(y,L)},E)
        filling=R.mul(R.mul(E,R.power(A,L-1)),{R.scale(y,-L)})
        assert R.mul(A,filling)==E and R.mul(B,filling)==E
        cases.append({'L':L,'n':2*R.n,'odd_norm_weight':len(E),
                      'cycle_weight':2*len(E),'is_boundary':True,
                      'displayed_filling_weight':len(filling),
                      'norm_sector_acyclic':True})
    report={'purpose':'Reject the false version of the twist lemma without its active-summand hypothesis',
            'minimum_distances_computed':False,'cases':cases}
    Path(__file__).with_name('odd_sector_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
