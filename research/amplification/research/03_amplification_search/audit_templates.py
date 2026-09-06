from audit_batch import ROOT,Engine,check_witness
import json

def main():
    data=json.loads((ROOT/'template_search_results.json').read_text());e=Engine();bases=set();count=0
    for r in data['results']:
        L=r['L'];A=tuple(map(tuple,r['A']));B=tuple(map(tuple,r['B']));At=tuple(map(tuple,r['At']));Bt=tuple(map(tuple,r['Bt']))
        assert sorted((a%L,b) for a,b in At)==sorted(A)
        assert sorted((a%L,b) for a,b in Bt)==sorted(B)
        key=(L,A,B)
        if key not in bases:
            lo=e.run(L,1,list(A),list(B),4)
            assert not lo['found'] and not lo['cutoff']
            check_witness(L,1,A,B,r['base']);assert len(r['base']['witness'])==6;bases.add(key)
        check_witness(2*L,1,At,Bt,r['cover']);assert len(r['cover']['witness'])<=14;count+=1
    e.close();out=dict(base_parameter_sets=len(bases),cover_instances=count,independently_audited_upper_witnesses=count,base_d=6,cover_upper_at_most=14)
    (ROOT/'template_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
