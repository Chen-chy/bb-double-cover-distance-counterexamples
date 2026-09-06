"""Reproduce the final exact certificates and independently audit retained data."""
from pathlib import Path
import subprocess,sys,json,os
ROOT=Path(__file__).resolve().parent

def main():
    # Final certificates always use the final deterministic default-order engine.
    os.environ.pop('BB_EXECUTABLE',None);os.environ.pop('BB_ORDER',None)
    for name in ('search','search_general','mitm'):
        subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra','-pedantic',str(ROOT/(name+'.cpp')),'-o',str(ROOT/name)],check=True)
    for name in ('verify_theorems.py','verify_search.py','independent_search.py'):
        subprocess.run([sys.executable,str(ROOT/name)],check=True)
    r=subprocess.check_output([str(ROOT/'mitm')],text=True)
    (ROOT/'reduced_code_mitm.json').write_text(r);print(r,end='')
    for seed in (9301,9302,9303,9304,9305):
        subprocess.run([sys.executable,str(ROOT/'audit_batch.py'),str(seed)],check=True)
    subprocess.run([sys.executable,str(ROOT/'audit_templates.py')],check=True)
    summary={str(seed):json.loads((ROOT/f'audit_{seed}.json').read_text()) for seed in (9301,9302,9303,9304,9305)}
    summary['templates']=json.loads((ROOT/'template_audit.json').read_text())
    (ROOT/'final_verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('All final certificate checks and retained-data audits passed.')
if __name__=='__main__':main()
