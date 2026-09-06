"""Reproduce both exhaustive checks and the independent arithmetic cross-checks.
Requires Python 3.10+, a C++17 g++ compiler, and SymPy for the third check.
The all-pairings verifier can also be compiled/run alone without Python packages.
"""
from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parent

def run(*args,stdout=None,stderr=None):
    subprocess.run(list(map(str,args)),cwd=ROOT,check=True,stdout=stdout,stderr=stderr)

def main():
    for source in ('verify6_all_pairings','enumerate6_bounded'):
        run('g++','-O3','-std=c++17',ROOT/(source+'.cpp'),'-o',ROOT/source)
    with (ROOT/'independent_pairings.json').open('w') as f:
        run(ROOT/'verify6_all_pairings',stdout=f)
    r=json.loads((ROOT/'independent_pairings.json').read_text())
    assert r['pairings_per_support_type']==11608920
    assert max(x['max_finite_order']for x in r['support_types'])==27
    assert max(x['max_torsion_times_range']for x in r['support_types'])==14
    run(sys.executable,ROOT/'generate_graphs.py')
    with (ROOT/'enumeration6_bounded.log').open('w')as f:
        run(ROOT/'enumerate6_bounded',ROOT/'graphs6.txt',ROOT/'rank2_candidates.jsonl',stderr=f)
    for name in ('filter6','certify_highrank6','verify_presentations_sympy','verify_frobenius'):
        run(sys.executable,ROOT/(name+'.py'))
    summary={
      'status':'all checks passed',
      'theorem':'Every valid binary strict-trinomial BB double cover with base distance six has cover distance at most 112.',
      'normalized_presentations':2488320,
      'all_pairing_checks':3*r['pairings_per_support_type'],
      'higher_rank_presentations_rechecked_with_full_Smith_form':684,
      'finite_power_cycle_crosschecks':json.loads((ROOT/'frobenius_verification.json').read_text())['counts']['cover_cases_checked'],
      'not_claimed':['optimality of 112','a finite universal amplification constant','an independent human referee or proof-assistant formalization']}
    (ROOT/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
