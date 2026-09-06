"""Brute-force cross-checks and retained exact numerical certificates."""
from pathlib import Path
from itertools import combinations
import random,json,subprocess
from algebra import Group,Code,poly,support
from scan import Engine,ROOT

def brute(code,bound):
    for w in range(1,bound+1):
        for inds in combinations(range(2*code.M),w):
            syndrome=0;word=0
            for i in inds:syndrome^=code.cols[i];word^=1<<i
            if syndrome==0 and not code.bd.contains(word):return word
    return None


def general_run(p,G,A,B,bound):
    s=' '.join(map(str,[G.l,G.m,len(A),len(B),*[z for pt in A+B for z in pt],bound,0]))
    p.stdin.write(s+'\n');p.stdin.flush();r=json.loads(p.stdout.readline());assert 'error' not in r;return r


def main():
    rng=random.Random(9333);e=Engine();p=subprocess.Popen([str(ROOT/'search_general')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
    count=0
    for l,m in [(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(3,2),(3,3)]:
        G=Group(l,m)
        for j in range(3):
            idsA=rng.sample(range(G.size),3);idsB=rng.sample(range(G.size),3)
            A=[(i//m,i%m) for i in idsA];B=[(i//m,i%m) for i in idsB];code=Code(G,poly(idsA),poly(idsB))
            r=e.run(l,m,A,B,6);w=brute(code,6);assert r['found']==(w is not None) and r['k']==code.k
            if r['found']:assert code.logical(poly(r['witness']))
            count+=1
            if G.size>=4:
                idsB=rng.sample(range(G.size),4);B=[(i//m,i%m) for i in idsB];code=Code(G,poly(idsA),poly(idsB))
                r=general_run(p,G,A,B,6);w=brute(code,6);assert r['found']==(w is not None) and r['k']==code.k
                if r['found']:assert code.logical(poly(r['witness']))
                count+=1
    exact=[]
    for L,A,B,d in [(39,[0,8,25],[0,2,13],6),(78,[0,8,25],[0,2,13],14)]:
        aa=[(i,0) for i in A];bb=[(i,0) for i in B];lo=e.run(L,1,aa,bb,d-2);hi=e.run(L,1,aa,bb,d)
        assert not lo['found'] and not lo['cutoff'] and hi['found']
        code=Code(Group(L),poly(A),poly(B));w=poly(hi['witness']);assert code.logical(w) and w.bit_count()==d
        exact.append(dict(L=L,A=A,B=B,k=code.k,d=d,lower=lo,upper=hi,u=support(w&code.mask),v=support(w>>L)))
    G=Group(39);A=[(i,0) for i in [0,5,28]];B=[(i,0) for i in [14,22,26,28]]
    lo=general_run(p,G,A,B,8);hi=general_run(p,G,A,B,9);assert not lo['found'] and not lo['cutoff'] and hi['found']
    code=Code(G,G.from_coords(A),G.from_coords(B));w=poly(hi['witness']);assert code.logical(w) and w.bit_count()==9
    exact.append(dict(label='reduced code, NOT a new BB amplification example',L=39,A=A,B=B,k=4,d=9,lower=lo,upper=hi))
    e.close();p.stdin.close();p.wait();out=dict(brute_force_comparisons=count,exact_examples=exact)
    (ROOT/'search_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
