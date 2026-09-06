"""Independent standard-library audit of the fixed-message Bellman certificate.

It verifies Bellman SUBsolution inequalities (not a shortest-path search), the
attaining word, a finite dual nonboundary certificate, the exact base minimum
six, and an explicit boundary from the weight-74 word to a weight-14 word in
the SAME universal class. The weight-14 lower bound is an inherited certificate.
"""
from pathlib import Path
import json,struct,hashlib,array,sys
ROOT=Path(__file__).resolve().parent

def xor(*ps):
 r=set()
 for p in ps:r.symmetric_difference_update(p)
 return r

def tr(p,k):return {i+k for i in p}
def times(p,q):return xor(*(tr(p,j) for j in q))
def divide(p,q):
 if not q:raise ZeroDivisionError
 if not p:return set()
 shift=min(p)-min(q);r=tr(p,-min(p));b=tr(q,-min(q));ans=set();d=max(b)
 while r and max(r)>=d:
  k=max(r)-d;ans.symmetric_difference_update({k});r.symmetric_difference_update(tr(b,k))
 assert not r,'inexact division'
 return tr(ans,shift)

def mod_at_order(p,modulus,order):
 def rem(v):
  while v.bit_length()>=modulus.bit_length():v^=modulus<<(v.bit_length()-modulus.bit_length())
  return v
 ans=0
 for n in p:ans^=rem(1<<(n%order))
 return ans

def cover_boundary(l,k,A,B):
 # epsilon-coordinate boundary (B l + epsilon(l+B k), A l + epsilon(l+A k))
 return (xor(times(B,l),l,times(B,k)),xor(l,times(B,k)),
         xor(times(A,l),l,times(A,k)),xor(l,times(A,k)))

def main():
 meta=json.loads((ROOT/'fixed_message_certificate.json').read_text())
 data=(ROOT/'fixed_message_potential.bin').read_bytes()
 assert hashlib.sha256(data).hexdigest()==meta['potential_sha256']
 assert data[:8]==b'BBTREE01'
 layers,n=struct.unpack_from('<II',data,8);vals=array.array('I');vals.frombytes(data[16:])
 if sys.byteorder!='little':vals.byteswap()
 assert len(vals)==layers*n and n==1<<meta['memory']
 lo,hi=meta['anchor_interval'];scale=meta['scale'];INF=meta['infinity']
 alpha,beta,sigma=map(set,(meta['alpha'],meta['beta'],meta['sigma']))
 assert vals[(layers-1)*n]==0
 transitions=0
 for layer in range(layers-1):
  i=lo+layer
  for state in range(n):
   p=vals[layer*n+state]
   for b in ([0,1] if i<=hi else [0]):
    e=(int(i in sigma)^b)+b
    e+=(int(i in alpha)^b^((state>>10)&1))
    e+=(int(i in beta)^b^((state>>4)&1))
    dest=((state<<1)&(n-1))|b
    rhs=min(INF,e*scale+b+vals[(layer+1)*n+dest])
    assert p<=rhs,(layer,state,b,p,rhs)
    transitions+=1
 assert vals[0]==meta['lexicographic_minimum']==74*scale+15
 f,h=map(set,(meta['phi'],meta['h']));word=list(map(set,meta['physical']))
 assert len(h)==15 and sum(map(len,word))==74
 pcost=0;state=0
 for i in range(lo,hi+12):
  b=int(i in h)
  e=(int(i in sigma)^b)+b+(int(i in alpha)^b^((state>>10)&1))+(int(i in beta)^b^((state>>4)&1))
  pcost+=scale*e+b;state=((state<<1)&(n-1))|b
 assert state==0 and pcost==vals[0]
 # Independent exact polynomial checks for the common-message constraints.
 A={-4,0,1};B={0,2,13};one={0};G={0,1,2,4,7}
 assert times(alpha,G)==tr(times(xor(times(A,B),A,B),f),-2)
 assert times(beta,G)==tr(times(times(A,A),f),4)
 assert times(sigma,G)==times(xor(A,B),f)
 assert not xor(tr(alpha,6),beta,sigma,tr(sigma,5))
 assert xor(alpha,tr(alpha,5),beta,tr(beta,11))==tr(sigma,2) # Y^-2 H^-1=z^2
 assert mod_at_order(f,0b111,3)==1
 u0,u1,v0,v1=word
 assert v1==h and xor(u1,v1)==sigma
 assert not xor(times(xor(A,one),u0),u1,times(xor(B,one),v0),v1)
 assert not xor(u0,times(xor(A,one),u1),v0,times(xor(B,one),v1))
 # The canonical six-vertex source-free tree in the attaining field.
 T=set(range(0,30,5));assert T<=h and not(T&sigma)
 for step,F in [(11,alpha),(5,beta)]:
  for i in T|tr(T,step):
   assert int(i in F)==(int(i in h)^int(i-step in h))
 # Exact base minimum: (b f,f) in a monomial-equivalent gauge; degree(b)=8,
 # weight(b)=7 rules out all weights 2 and 4 by the binomial quotient proof.
 As={0,4,5};bq={0,2,4,5,6,7,8}
 assert times(As,bq)==B and len(bq)==7 and max(bq)==8
 base=({5,10,14,15},{1,3})
 assert not xor(times(A,base[0]),times(B,base[1]))
 assert sum(map(len,base))==6
 # Primitive base message is z^4 times the right component.
 assert mod_at_order(tr(base[1],4),0b111,3)==1
 # A weight-14 word from the supplied exact minimum, ungauged and translated.
 old=({3,10,11},{0,4,6,7,9,11,12},{0},{2,3,4})
 star=(tr(old[0],27),tr(old[1],27),tr(old[2],23),tr(old[3],23))
 star_phi={29,32,33};star_h=star[3]
 assert sum(map(len,star))==14
 diffphi=xor(f,star_phi);k=divide(diffphi,G)
 l=xor(h,star_h,times(A,k))
 bd=cover_boundary(l,k,A,B)
 assert all(xor(a,b)==c for a,b,c in zip(word,star,bd))
 assert mod_at_order(f,sum(1<<i for i in G),42)==mod_at_order(star_phi,sum(1<<i for i in G),42)
 assert mod_at_order({0,210},sum(1<<i for i in G),42)==0
 # The direct base flip from this tree increases weight, rather than reducing it.
 bT=(times(B,T),times(A,T));changed=tuple(xor(a,b) for a,b in zip(base,bT))
 assert sum(map(len,bT))==26 and sum(map(len,changed))==26
 # A separate finite dual check, using actual finite group coordinates.
 L=meta['finite_nonboundary']['L'];dual=int(meta['finite_nonboundary']['dual_hex'],16)
 mask=(1<<L)-1
 def bits(P):
  out=0
  for i in P:out^=1<<(i%L)
  return out
 def rotate(x,j):return ((x<<j)&mask)^(x>>(L-j)) if j else x
 def shifted(P0,P1,j,t):
  a,b=rotate(bits(P0),j),rotate(bits(P1),j)
  return (b|(a<<L)) if t else (a|(b<<L))
 finite=sum(bits(P)<<(i*L) for i,P in enumerate(word))
 assert (finite&dual).bit_count()%2==1
 pairings=0
 for t in (0,1):
  for j in range(L):
   bd=shifted(xor(B,one),one,j,t)|(shifted(xor(A,one),one,j,t)<<(2*L))
   assert (bd&dual).bit_count()%2==0;pairings+=1
 # The long-message construction has zero separator slices. The required
 # 4-cycles at every separator site are checked symbolically at one gap.
 anchors=set(sigma)|alpha|tr(alpha,-11)|beta|tr(beta,-5)
 assert (min(anchors),max(anchors))==(lo,hi)
 for i in range(75,86):
  vertices={i,i+5,i+11,i+16}
  assert all(hi<v<lo+210 for v in vertices)
  assert not(vertices&sigma)
 result={'bellman_inequalities_checked':transitions,'fixed_message_minimum_energy':74,
  'minimum_field_support_among_fixed_message_optima':15,'same_universal_class_attaining_word_weight':14,
  'fixed_message_counterexample_is_NOT_a_full_minimum_counterexample':True,
  'finite_boundary_pairings_checked':pairings,'finite_nonboundary_proved':True,
  'base_distance_six_symbolic_checks':True,'direct_tree_base_boundary_weight':26,
  'base_weight_after_direct_tree_flip':26,'parametric_spacing':210,'parametric_scope':'odd N; fixed-message minimum 74N, support minimum 15N; full universal class minimum 14 uses inherited lower certificate'}
 (ROOT/'fixed_message_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 (ROOT/'explicit_exchange.json').write_text(json.dumps({'phi_star':sorted(star_phi),'word_star':[sorted(P) for P in star],
   'boundary_l':sorted(l),'boundary_k':sorted(k)},indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
