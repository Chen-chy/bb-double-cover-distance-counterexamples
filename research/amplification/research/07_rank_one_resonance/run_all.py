from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for name in ('verify_structure.py','verify_lifts.py','check_seed_coordinates.py','verify_finite_parity.py','verify_sharpness.py','audit_certificates.py'):
    result=subprocess.run([sys.executable,str(root/name)],cwd=root,check=True,text=True,capture_output=True)
    (root/(name.removesuffix('.py')+'.log')).write_text(result.stdout)
    print(name+'\n'+result.stdout)
