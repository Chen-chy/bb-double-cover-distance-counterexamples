#!/usr/bin/env python3
"""Run the two standalone certificates, preserve outputs, and compare artifacts."""
import hashlib,json,platform,subprocess,sys,time
from pathlib import Path

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    root=Path(__file__).resolve().parent
    metadata={'python':sys.version,'platform':platform.platform(),'executions':[]}
    for name,output,log in [('verify_lower_bitset.py','bitset_output','bitset_run.txt'),
                            ('verify_lower_polynomial.py','polynomial_output','polynomial_run.txt')]:
        start=time.monotonic()
        with (root/log).open('wb') as stdout:
            run=subprocess.run([sys.executable,str(root/name),'--output-dir',str(root/output)],stdout=stdout,stderr=subprocess.STDOUT)
        ok=(run.returncode==0 and (root/log).read_text().splitlines()[-1]=='BB_LOWER_BOUND_COUNTEREXAMPLE_VERIFIED')
        metadata['executions'].append(dict(script=name,returncode=run.returncode,success=ok,
                    seconds=round(time.monotonic()-start,3),script_sha256=sha(root/name),stdout_sha256=sha(root/log)))
        if not ok:
            (root/'EXECUTION_METADATA.json').write_text(json.dumps(metadata,indent=2)+'\n')
            raise RuntimeError(f'{name} failed; inspect {log}')
        print(name,'PASS',flush=True)
    comparisons={}
    for file in ['base_HX.txt','base_HZ.txt','cover_HX.txt','cover_HZ.txt','base_circuits.txt','cover_circuits.txt']:
        a,b=root/'bitset_output'/file,root/'polynomial_output'/file
        if a.read_bytes()!=b.read_bytes():raise RuntimeError(f'Independent mismatch: {file}')
        comparisons[file]={'byte_identical':True,'sha256':sha(a)}
    a=json.loads((root/'bitset_output/report.json').read_text());b=json.loads((root/'polynomial_output/report.json').read_text())
    for code in ('base','cover'):
        for field in ('n','k','d','rank_HX','rank_HZ','circuits'):
            if a['codes'][code][field]!=b['codes'][code][field]:raise RuntimeError(f'Report mismatch: {code}/{field}')
    metadata['independent_comparison']=comparisons
    metadata['ranks_distances_circuit_counts_identical']=True
    (root/'EXECUTION_METADATA.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print('INDEPENDENT_LOWER_BOUND_CERTIFICATES_AGREE',flush=True)

if __name__=='__main__':main()
