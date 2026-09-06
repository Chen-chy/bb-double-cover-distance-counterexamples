"""Generate complete shortest-path closure certificates for five compact metrics.
Uses a C++17 compiler; the independent auditor itself uses only Python.
"""
from pathlib import Path
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parent
CASES=[
 dict(name='base_full',kind='base',mod=7,target=7,kill=1,coef0=1,coef1=0,bound=6,expect=6),
 dict(name='base_resonant_purified',kind='base',mod=49,target=7,kill=11,coef0=1,coef1=0,bound=12,expect=12),
 dict(name='base_other_purified',kind='base',mod=49,target=11,kill=7,coef0=1,coef1=0,bound=10,expect=10),
 dict(name='cover_full',kind='cover',mod=7,target=7,kill=1,coef0=1,coef1=1,bound=14,expect=14),
 dict(name='cover_resonant_purified',kind='cover',mod=475,target=7,kill=69,coef0=219,coef1=125,bound=16,expect=16),
]
def main():
 (ROOT/'certificates').mkdir(exist_ok=True)
 subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'trellis_exact.cpp'),'-o',str(ROOT/'trellis_exact')],check=True)
 out=[]
 for spec in CASES:
  cov=spec['kind']=='cover';A0,A1,B0,B1=(33,16,8196,1) if cov else (49,0,8197,0)
  path=ROOT/'certificates'/f"{spec['name']}.bin"
  args=[int(cov),A0,A1,B0,B1,spec['mod'],spec['bound'],8_000_000,spec['target'],spec['kill'],spec['coef0'],spec['coef1'],path]
  result=json.loads(subprocess.check_output([str(ROOT/'trellis_exact'),*map(str,args)],text=True))
  assert result['certified'] and not result['capped'] and result['distance']==spec['expect']
  row=dict(spec,A0=A0,A1=A1,B0=B0,B1=B1,result=result,certificate=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
  out.append(row)
  print(spec['name'],result['distance'],result['certificate_states'],flush=True)
 (ROOT/'exact_results.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
