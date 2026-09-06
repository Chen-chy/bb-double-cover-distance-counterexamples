"""Exact nonlocal reduction of a two-step signed graph with unit/two-unit fields.

No claim about minimization over BB homology messages is made here. For each
fixed message, source spins and a maximum independent set give the COMPLETE
minimum over the remaining boundary variables.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    sign: int
    kind: int

class Model:
    def __init__(self, steps, edge_signs, sources):
        if len(steps)!=2 or any(s==0 for s in steps):
            raise ValueError('Two nonzero steps required')
        self.steps=tuple(steps)
        self.signs=tuple(frozenset(F) for F in edge_signs)
        self.sources=frozenset(sources)
        anchors=set(self.sources)
        for step,F in zip(self.steps,self.signs):
            for i in F:anchors.update((i,i-step))
        self.lo=min(anchors) if anchors else 0
        self.hi=max(anchors) if anchors else -1
        self.vertices=tuple(range(self.lo,self.hi+1))
        edges=[]
        for typ,(step,F) in enumerate(zip(self.steps,self.signs)):
            indices=set(self.vertices)|{i+step for i in self.vertices}
            for i in sorted(indices):
                edges.append(Edge(i,i-step,int(i in F),typ))
        self.edges=tuple(edges)

    def energy(self,h):
        h=set(h)
        if not h<=set(self.vertices):raise ValueError('Use the proved anchor interval')
        return sum(e.sign^int(e.u in h)^int(e.v in h) for e in self.edges)+len(h^self.sources)+len(h)

    def candidates(self):
        free=set(self.vertices)-self.sources
        adj={v:set() for v in free}
        pinned=set()
        for e in self.edges:
            if e.sign:continue
            if e.u in free and e.v in free:
                adj[e.u].add(e.v);adj[e.v].add(e.u)
            elif e.u in free and e.v not in self.sources:pinned.add(e.u)
            elif e.v in free and e.u not in self.sources:pinned.add(e.v)
        unseen=set(free);components=[]
        while unseen:
            root=unseen.pop();C={root};todo=[root]
            while todo:
                v=todo.pop()
                for w in adj[v]:
                    if w in unseen:unseen.remove(w);C.add(w);todo.append(w)
            if C&pinned:continue
            internal=[e for e in self.edges if e.u in C and e.v in C]
            if len(internal)!=len(C)-1 or any(e.sign for e in internal):continue
            needs={};valid=True
            for e in self.edges:
                if (e.u in C)==(e.v in C):continue
                out=e.v if e.u in C else e.u
                want=1^e.sign
                if out in self.sources:
                    if out in needs and needs[out]!=want:valid=False;break
                    needs[out]=want
                elif want:valid=False;break # zero edge to nonsource outside C is forbidden
            if valid:components.append((frozenset(C),needs))
        components.sort(key=lambda c:tuple(sorted(c[0])))
        owners={v:i for i,(C,_) in enumerate(components) for v in C}
        conflicts=set()
        for e in self.edges:
            a=owners.get(e.u);b=owners.get(e.v)
            if a is not None and b is not None and a!=b:
                assert e.sign==1
                conflicts.add(tuple(sorted((a,b))))
        return components,conflicts

    def exact_reduced(self):
        """Exhaustive source/MIS evaluation, intended for small audit inputs."""
        comps,conflicts=self.candidates();src=sorted(self.sources)
        best=(10**9,10**9);best_h=None
        for mask in range(1<<len(src)):
            x={v for i,v in enumerate(src) if mask>>i&1}
            eligible=[i for i,(_,needs) in enumerate(comps) if all(int(v in x)==b for v,b in needs.items())]
            base=self.energy(x)
            for sub in range(1<<len(eligible)):
                I={i for bit,i in enumerate(eligible) if sub>>bit&1}
                if any(a in I and b in I for a,b in conflicts):continue
                h=x|set().union(*(comps[i][0] for i in I)) if I else x.copy()
                en=base-2*len(I)
                assert self.energy(h)==en
                value=(en,len(h))
                if value<best:best=value;best_h=h
        return best,best_h
