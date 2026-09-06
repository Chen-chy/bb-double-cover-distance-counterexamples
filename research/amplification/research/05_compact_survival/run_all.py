"""Run all retained supplementary exact checks."""
from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parent
for script in ['verify_mechanisms.py','verify_finite_covers.py','audit_finite_certificates.py','verify_weight8_testbed.py']:
    result=subprocess.run([sys.executable,str(ROOT/script)],check=True,capture_output=True,text=True,cwd=ROOT)
    (ROOT/(Path(script).stem+'.log')).write_text(result.stdout)
    print(script+': passed',flush=True)
summary={'all_checks_passed':True,
         'proof_type':'uniform symbolic proof with supplementary exact arithmetic checks',
         'minimum_distance_searches_performed':False,
         'finite_cover_audit':json.loads((ROOT/'finite_certificate_audit.json').read_text()),
         'finite_cover_summary':json.loads((ROOT/'finite_cover_summary.json').read_text())}
(ROOT/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
