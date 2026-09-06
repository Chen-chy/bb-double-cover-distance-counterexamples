"""Finite exact audits of the uniformly proved separated-message family.
No finite-instance check substitutes for the separator proof in REPORT.md."""
from pathlib import Path
import json
from audit_fixed_certificate import xor,tr,times,divide,mod_at_order,cover_boundary
ROOT=Path(__file__).resolve().parent

def main():
 d=json.loads((ROOT/'fixed_message_certificate.json').read_text())
 ex=json.loads((ROOT/'explicit_exchange.json').read_text())
 f0=set(d['phi']);h0=set(d['h']);w0=list(map(set,d['physical']))
 G={0,1,2,4,7};A={-4,0,1};B={0,2,13};Gbits=sum(1<<i for i in G)
 star=list(map(set,ex['word_star']));fs=set(ex['phi_star']);hs=star[3]
 output=[]
 for N in (1,3,5,11):
  f=xor(*(tr(f0,210*j) for j in range(N)));h=xor(*(tr(h0,210*j) for j in range(N)))
  word=[xor(*(tr(P,210*j) for j in range(N))) for P in w0]
  assert sum(map(len,word))==74*N and len(h)==15*N
  assert mod_at_order(f,Gbits,42)==mod_at_order(fs,Gbits,42)
  k=divide(xor(f,fs),G);l=xor(h,hs,times(A,k))
  assert all(xor(P,Q)==C for P,Q,C in zip(word,star,cover_boundary(l,k,A,B)))
  sigma=xor(*(tr(set(d['sigma']),210*j) for j in range(N)))
  al=xor(*(tr(set(d['alpha']),210*j) for j in range(N)))
  be=xor(*(tr(set(d['beta']),210*j) for j in range(N)))
  for j in range(N-1):
   for i in range(75+210*j,86+210*j):
    corners={i,i+5,i+11,i+16}
    assert not(corners&sigma)
    assert not ({i+11,i+16}&al)
    assert not ({i+5,i+16}&be)
  output.append({'N':N,'fixed_message_minimum_from_uniform_proof':74*N,
                 'minimum_field_support_from_uniform_proof':15*N,
                 'same_universal_class':True,'explicit_boundary_to_weight14':True})
 (ROOT/'parametric_verification.json').write_text(json.dumps(output,indent=2)+'\n')
 print(json.dumps(output,indent=2))
if __name__=='__main__':main()
