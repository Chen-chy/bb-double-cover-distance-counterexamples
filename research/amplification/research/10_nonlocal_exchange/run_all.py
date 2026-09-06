#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parent
scripts=['verify_identities.py','verify_forest.py','verify_tree_contraction.py',
         'audit_triangle.py','audit_fixed_certificate.py','verify_parametric.py',
         'inherited_certificates/audit_certificates.py']
for script in scripts:
 print('\n--- '+script+' ---',flush=True)
 subprocess.run([sys.executable,str(ROOT/script)],check=True,cwd=ROOT)
result={'status':'all retained audits passed','factor_three_status':'unresolved',
        'new_counterexample_above_three':False,'audited_scripts':scripts}
(ROOT/'verification_summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
