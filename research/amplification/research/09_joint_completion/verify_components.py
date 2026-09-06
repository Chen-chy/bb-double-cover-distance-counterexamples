"""Independent exhaustive checks of the signed-cut component theorem.

The graph is infinite, with two odd steps and parallel edges retained. Spins
are enumerated in a finite interval; all edges to its exterior are included.
The theorem only uses removal of a component, so every reported check is
valid for this finite-domain optimization too. The uniform infinite-domain
claim is proved in REPORT.md, not inferred from these examples.
"""
from __future__ import annotations
from pathlib import Path
from itertools import product
import json, random


def edges_touching(vertices: set[int], steps: tuple[int, int]):
    return {(kind, i) for kind, step in enumerate(steps)
            for v in vertices for i in (v, v + step)}


def endpoints(edge, steps):
    kind, i = edge
    return i, i - steps[kind]


def energy(h, sources, negative, steps):
    edges = negative | edges_touching(h, steps)
    cost = sum(int((e in negative) ^ ((endpoints(e,steps)[0] in h)
                                     ^ (endpoints(e,steps)[1] in h)))
               for e in edges)
    return cost + len(h ^ sources) + len(h)


def components(h, steps):
    remaining=set(h)
    while remaining:
        root=next(iter(remaining)); remaining.remove(root)
        component={root}; todo=[root]
        while todo:
            i=todo.pop()
            for step in steps:
                for j in (i-step, i+step):
                    if j in remaining:
                        remaining.remove(j);component.add(j);todo.append(j)
        yield component


def main():
    rng=random.Random(6062026)
    cases=0; components_checked=0; source_free=0; configurations=0
    for steps in ((1,3),(1,5),(3,5),(-1,3),(-3,-1),(-3,3)):
        sites=list(range(-4,5)); universe=set(sites)
        all_edges=sorted(edges_touching(universe,steps))
        for trial in range(16):
            sources={i for i in sites if rng.randrange(4)==0}
            negative={e for e in all_edges if rng.randrange(3)==0}
            best=None;opt=None
            for bits in product((0,1),repeat=len(sites)):
                h={i for i,b in zip(sites,bits) if b}
                key=(energy(h,sources,negative,steps),len(h))
                if best is None or key<best:best,opt=key,h
                configurations+=1
            assert opt is not None
            assert len(opt)<=len(sources)+len(negative)//2
            for R in components(opt,steps):
                incident=edges_touching(R,steps)
                internal={e for e in incident if all(i in R for i in endpoints(e,steps))}
                cut=incident-internal
                beta=len(internal)-len(R)+1;q=len(R & sources)
                improvement=energy(opt-R,sources,negative,steps)-energy(opt,sources,negative,steps)
                assert improvement==2*len(cut & negative)-len(cut)-2*len(R-sources)
                assert improvement>=2 and beta<=q
                if not q:
                    assert beta==0 and cut<=negative and not(internal & negative)
                    source_free+=1
                anchors=set(sources)
                for e in negative:anchors.update(endpoints(e,steps))
                assert R & anchors
                components_checked+=1
            cases+=1
    # A tree of arbitrary length can occur if one keeps only a generic cut
    # model. This control is not asserted to be canonical BB message data.
    for n in range(1,9):
        R={3*i for i in range(n)};steps=(3,5)
        negative={e for e in edges_touching(R,steps)
                  if sum(i in R for i in endpoints(e,steps))==1}
        assert energy(R,set(),negative,steps)==2*n
        assert energy(set(),set(),negative,steps)==2*n+2
    result={'status':'all exact checks passed','finite_domain_cases':cases,
            'spin_configurations':configurations,'optimal_components_checked':components_checked,
            'source_free_components_checked':source_free,
            'generic_tree_controls':8}
    Path(__file__).with_name('component_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
