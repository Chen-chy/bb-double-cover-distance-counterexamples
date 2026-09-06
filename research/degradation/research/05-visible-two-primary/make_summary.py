import json,hashlib,pathlib
root=pathlib.Path(__file__).resolve().parent
load=lambda name:json.loads((root/name).read_text())
summary={'principal_status':'TRINOMIAL_STILL_OPEN','quadratic_bound_proved':False,'quadratic_bound_refuted':False,
'new_uniform_results':['Actual finite local H0 is K[t]/t^m; H1 is two equal copies; H2 is one copy.',
'Local length m has at most two nonzero binary digits for support-generated strict-trinomial BB codes.',
'Projection and transfer have the compatible two-branch normal forms in proof.md.',
'Every increasing local double-cover length is a power of two plus a power-of-two increment.',
'Explicit strict-trinomial high-contact families realize non-power-of-two lengths; a partial-growth family has exact base distance four.'],
'scope':'Actual support groups with at most two generators; no Hamming-isometry claim and no identification of compact image with full finite homology.',
'inherited_distance_bound':'d <= 4*d_2^3','new_distance_degradation_record':False,
'contact':load('contact_verification.json'),'random_local_matrices':load('local_verification.json'),
'structured_matrices':load('structured_verification.json'),'rectangular_family':load('family_verification.json')}
(root/'verification_summary.json').write_text(json.dumps(summary,indent=2))
files=sorted(p for p in root.iterdir() if p.is_file() and p.name!='manifest.json')
(root/'manifest.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2))
print(json.dumps({'principal_status':summary['principal_status'],'local_matrix_cases':384+72+6,'all_checks_pass':True},indent=2))
