"""Run all retained exact checks; no nonstandard Python packages are needed."""
from pathlib import Path
import subprocess,sys,json
HERE=Path(__file__).resolve().parent
scripts=['verify_sparse_generators.py','verify_embeddings.py','field_distance.py',
         'verify_finite_replacement.py','audit_replacement_certificates.py','verify_sharpness.py']
for script in scripts:
    result=subprocess.run([sys.executable,str(HERE/script)],cwd=HERE,text=True,capture_output=True)
    (HERE/(Path(script).stem+'.log')).write_text(result.stdout+result.stderr)
    if result.returncode:
        print(result.stdout);print(result.stderr,file=sys.stderr)
        raise SystemExit(result.returncode)
    print(script+': passed',flush=True)
summary={'status':'all checks passed','scripts':scripts,
         'sparse_generator_cases':json.loads((HERE/'sparse_generator_checks.json').read_text())['cases'],
         'generic_embedding_checks':json.loads((HERE/'embedding_checks.json').read_text())['random_polynomials'],
         'finite_replacement':json.loads((HERE/'finite_replacement_summary.json').read_text()),
         'independent_audit':json.loads((HERE/'finite_replacement_audit.json').read_text())}
(HERE/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
