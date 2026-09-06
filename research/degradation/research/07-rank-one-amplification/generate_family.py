from try_trellis import run
from core import poly, gcd, exact, square, supp, cover_generator
import json
from pathlib import Path
A=poly(0,2,7);B=poly(0,1,8);c=gcd(A,B)
base=run([[exact(B,c),exact(A,c)]],[1],c,'base_potential.bin')
cols,delta=cover_generator(A,B)
cover=run(cols,[1,0],c,'cover_potential.bin')
row=dict(A=supp(A),B=supp(B),c=supp(c),delta=supp(delta),base=base,cover=cover)
Path('family_certificate.json').write_text(json.dumps(row,indent=2))
print('Base relative Laurent distance:',base['distance'])
print('Cover relative Laurent distance:',cover['distance'])
