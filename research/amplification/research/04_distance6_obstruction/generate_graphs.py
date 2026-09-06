"""Generate all connected loopless labeled cubic multigraphs on six vertices."""
from pathlib import Path
from itertools import combinations
import json
ROOT=Path(__file__).parent

def main():
    edges=list(combinations(range(6),2));graphs=[]
    def visit(i,degree,multiplicity):
        if i==len(edges):
            if any(degree):return
            seen={0}
            while True:
                before=len(seen)
                for (a,b),m in zip(edges,multiplicity):
                    if m and (a in seen or b in seen):seen.update((a,b))
                if len(seen)==before:break
            if len(seen)==6:
                graphs.append([e for e,m in zip(edges,multiplicity)for _ in range(m)])
            return
        a,b=edges[i]
        for m in range(min(degree[a],degree[b])+1):
            degree[a]-=m;degree[b]-=m
            possible=all(degree[v]<=sum(min(degree[v],degree[w])for e in edges[i+1:]if v in e for w in e if w!=v)for v in range(6))
            if possible:visit(i+1,degree,multiplicity+[m])
            degree[a]+=m;degree[b]+=m
    visit(0,[3]*6,[])
    assert len(graphs)==640
    (ROOT/'graphs6.json').write_text(json.dumps(graphs)+'\n')
    (ROOT/'graphs6.txt').write_text(str(len(graphs))+'\n'+'\n'.join(' '.join(str(c)for e in g for c in e)for g in graphs)+'\n')
    print('connected labeled cubic multigraphs:',len(graphs))
if __name__=='__main__':main()
