from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent
result={
 'principal_status':'TRINOMIAL_STILL_OPEN',
 'quadratic_bound_proved':False,
 'quadratic_bound_refuted':False,
 'new_theorems':[
  'Compact projection is injective for support-generated rank-one presentations with odd torsion, under term-preserving 2-group quotients.',
  'A superquadratic counterexample must have a mixed finite/strip incidence presentation with visible 2-primary torsion.',
  'For principal period doubles, lost compact homology is exactly f*H1/f^2*H1; Tor-created homology remains a separate term.',
  'For cyclic torsion with A=1+t+z, compact homology is F2[t]/g and projection loss is the exact gcd-degree difference in the proof.',
  'No quadratic cofactor estimate follows from the short-relation-row hypothesis alone, even after changing the relation basis.',
  'A strict-trinomial torsion-changing quotient can kill the compact image even when universal H1 is a simple module.'
 ],
 'inherited_universal_bound':'d <= 4*d_2^3',
 'inherited_scale':'gamma_3(N) >= max(min(1/12,20/N), N^(-2/3), c0*N^(-1/2))',
 'inherited_upper_ratio':'6/7 at supplied certification status; not re-certified here',
 'vanishing_ratio_family_found':False,
 'new_exact_distance_record':False,
 'odd_torsion_tests':json.loads((p/'verification_summary.json').read_text()),
 'independent_matrix_tests':json.loads((p/'independent_verification.json').read_text()),
 'cyclic_torsion_tests':json.loads((p/'cyclic_strip_verification.json').read_text()),
}
(p/'summary.json').write_text(json.dumps(result,indent=2))
manifest={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.iterdir()) if f.is_file() and f.name!='manifest.json'}
(p/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('Wrote summary.json and manifest.json')
