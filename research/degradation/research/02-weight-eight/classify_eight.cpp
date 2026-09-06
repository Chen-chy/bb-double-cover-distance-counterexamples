#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using V=array<long long,4>;using M=array<V,5>;
long long checked(__int128 x){assert(x>=-1000000000000LL && x<=1000000000000LL);return (long long)x;}
V zero={0,0,0,0}; V add(V a,V b){for(int i=0;i<4;i++)a[i]=checked((__int128)a[i]+b[i]);return a;}V sub(V a,V b){for(int i=0;i<4;i++)a[i]=checked((__int128)a[i]-b[i]);return a;}V mul(V a,long long x){for(auto &v:a)v=checked((__int128)v*x);return a;}
long long floordiv(long long a,long long b){long long q=a/b,r=a%b;return q-(r<0);}
struct Lattice {
 M rows;vector<int> piv;int rank;long long torsion;
 Lattice(M a): rows(a) {
  int k=0;
  for(int j=0;j<4;j++) {
   while(true){int z=-1;for(int i=k;i<5;i++)if(rows[i][j]&&(z<0||abs(rows[i][j])<abs(rows[z][j])))z=i;if(z<0)break;
    swap(rows[k],rows[z]);bool again=false;
    for(int i=k+1;i<5;i++)if(rows[i][j]) {long long q=rows[i][j]/rows[k][j];rows[i]=sub(rows[i],mul(rows[k],q));if(rows[i][j])again=true;}
    if(!again)break;
   }
   if(!rows[k][j])continue;
   if(rows[k][j]<0)rows[k]=mul(rows[k],-1);
   for(int i=0;i<k;i++){long long q=floordiv(rows[i][j],rows[k][j]);rows[i]=sub(rows[i],mul(rows[k],q));}
   piv.push_back(j);k++;if(k==4)break;
  }
  rank=k;
  for(auto row:rows)for(auto x:row)assert(x>=-10000 && x<=10000);
  torsion=0;
  for(int mask=0;mask<16;mask++)if(__builtin_popcount((unsigned)mask)==k) {
   vector<int> cols;for(int j=0;j<4;j++)if(mask>>j&1)cols.push_back(j);
   long long d=0;vector<int> perm(k);iota(perm.begin(),perm.end(),0);
   do{long long t=1;int inv=0;for(int i=0;i<k;i++){t*=rows[i][cols[perm[i]]];for(int j=0;j<i;j++)if(perm[j]>perm[i])inv++;}d+=(inv%2?-t:t);}while(next_permutation(perm.begin(),perm.end()));
   torsion=gcd(torsion,abs(d));
  }
 }
 V norm(V v) const {for(int i=0;i<rank;i++){long long q=floordiv(v[piv[i]],rows[i][piv[i]]);v=sub(v,mul(rows[i],q));}return v;}
 bool member(V v) const{return norm(v)==zero;}
 bool order2power(V v)const{long long p=1;while(p<torsion)p*=2;return member(mul(v,p));}
 string key()const{ostringstream ss;for(int i=0;i<4;i++)for(auto x:rows[i])ss<<x<<',';return ss.str();}
};
string sv(V a){ostringstream s;for(auto x:a)s<<x<<',';return s.str();}
using Point=pair<int,V>;
vector<Point> boundary(V t,const Lattice& lat,const array<V,3>& A,const array<V,3>& B){vector<Point> out;for(auto b:B)out.push_back({0,lat.norm(add(t,b))});for(auto a:A)out.push_back({1,lat.norm(add(t,a))});sort(out.begin(),out.end());return out;}
vector<Point> xorsets(const vector<Point>& a,const vector<Point>& b){vector<Point> c;set_symmetric_difference(a.begin(),a.end(),b.begin(),b.end(),back_inserter(c));return c;}
int inverses[101];
int modrank3(M const&a){
 int rr[5][4];for(int i=0;i<5;i++)for(int j=0;j<4;j++){rr[i][j]=a[i][j]%101;if(rr[i][j]<0)rr[i][j]+=101;}
 int k=0;for(int j=0;j<4;j++){int p=k;while(p<5&&!rr[p][j])p++;if(p==5)continue;for(int z=j;z<4;z++)swap(rr[k][z],rr[p][z]);int in=inverses[rr[k][j]];for(int i=k+1;i<5;i++)if(rr[i][j]){int c=(rr[i][j]*in)%101;for(int z=j+1;z<4;z++){rr[i][z]=(rr[i][z]-c*rr[k][z])%101;if(rr[i][z]<0)rr[i][z]+=101;}rr[i][j]=0;}k++;if(k==3)return k;}return k;
}
int main(int argc,char**argv){
 for(int i=1;i<101;i++)for(int j=1;j<101;j++)if((i*j)%101==1)inverses[i]=j;

 string root=argc>1?argv[1]:"."; if(root.back()!='/') root+="/";
 ifstream in(root+"graph_multiplicities_8.txt"); if(!in){cerr<<"Missing graph_multiplicities_8.txt"<<endl; return 2;} vector<vector<pair<int,int>>> graphs;for(int g=0;g<20;g++){vector<pair<int,int>> e;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++){int m;in>>m;while(m--)e.push_back({i,j});}graphs.push_back(e);}
 vector<array<int,3>> perms;array<int,3> p={0,1,2};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 map<string,long long> counts;set<string> unique;ofstream out(root+"highrank_eight.tsv");
 ifstream colorin(root+"colorings_8.txt"); int gi,r,mask; int lastg=-1; while(colorin>>gi>>r>>mask) { if(gi!=lastg){cerr<<"starting graph "<<gi<<" unique="<<unique.size()<<endl;lastg=gi;}
  auto edges=graphs[gi];array<vector<int>,8> inc;for(int e=0;e<12;e++){inc[edges[e].first].push_back(e);inc[edges[e].second].push_back(e);}
  array<int,8> parent,pe;parent.fill(-2);parent[0]=-1;vector<int> bfs={0};set<int> tree;for(int z=0;z<(int)bfs.size();z++){int i=bfs[z];for(auto e:inc[i]){int j=edges[e].first+edges[e].second-i;if(parent[j]==-2){parent[j]=i;pe[j]=e;tree.insert(e);bfs.push_back(j);}}}
  vector<int> cotree;for(int e=0;e<12;e++)if(!tree.count(e))cotree.push_back(e);
  {
   array<int,8> block;int fixed[2]={-1,-1};vector<int> vary;for(int i=0;i<8;i++){block[i]=(mask>>i)&1;if(fixed[block[i]]<0)fixed[block[i]]=i;else vary.push_back(i);}
   assert(vary.size()==6);
   for(int pn=0;pn<46656;pn++) {
    counts[to_string(r)+":total"]++;
    array<array<V,12>,8> labels;
    int pp=pn;array<int,8> pi;pi.fill(0);for(int i:vary){pi[i]=pp%6;pp/=6;}
    for(int i=0;i<8;i++)for(int j=0;j<3;j++){V v=zero;int term=perms[pi[i]][j];if(term)v[2*block[i]+term-1]=1;labels[i][inc[i][j]]=v;}
    array<V,8> pos;pos[0]=zero;for(int jj=1;jj<8;jj++){int j=bfs[jj],i=parent[j],e=pe[j];pos[j]=add(pos[i],sub(labels[i][e],labels[j][e]));}
    M rel;for(int t=0;t<5;t++){int e=cotree[t],a=edges[e].first,b=edges[e].second;rel[t]=sub(add(pos[a],labels[a][e]),add(pos[b],labels[b][e]));}
    if(modrank3(rel)>=3){counts[to_string(r)+":rank_at_least_3"]++;continue;}
    Lattice lat(rel); if(lat.rank>=3){counts[to_string(r)+":exact_rank_at_least_3"]++;continue;}
    array<V,3> A={zero,V{1,0,0,0},V{0,1,0,0}},B={zero,V{0,0,1,0},V{0,0,0,1}};
    bool invalid=false,unit=false;for(auto S:{A,B})for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){V v=sub(S[i],S[j]);if(lat.member(v))invalid=true;if(lat.order2power(v))unit=true;}
    if(invalid){counts[to_string(r)+":invalid_terms"]++;continue;}
    for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)if(block[i]==block[j]&&lat.member(sub(pos[i],pos[j])))invalid=true;
    if(invalid){counts[to_string(r)+":invalid_columns"]++;continue;}
    if(unit){counts[to_string(r)+":unit"]++;continue;}
    vector<Point>w;for(int i=0;i<8;i++)w.push_back({block[i],lat.norm(pos[i])});sort(w.begin(),w.end());
    // Translation normalize: minimum lexicographic orbit representative, independently of point block.
    vector<Point> wmin=w;for(auto point:w){vector<Point> tr;for(auto q:w)tr.push_back({q.first,lat.norm(sub(q.second,point.second))});sort(tr.begin(),tr.end());wmin=min(wmin,tr);}w=wmin;
    string key=to_string(r)+":"+lat.key()+":";for(auto q:w)key+=to_string(q.first)+","+sv(q.second)+";";
    if(!unique.insert(key).second){counts[to_string(r)+":duplicates"]++;continue;}
    set<V> cand;for(auto q:w)for(auto t:(q.first==0?B:A))cand.insert(lat.norm(sub(q.second,t)));
    vector<vector<Point>> bs;int fill=0; int maxov=0;vector<V> cv(cand.begin(),cand.end());for(auto c:cv){bs.push_back(boundary(c,lat,A,B));if(bs.back()==w)fill=1; vector<Point> inter;set_intersection(bs.back().begin(),bs.back().end(),w.begin(),w.end(),back_inserter(inter));maxov=max(maxov,(int)inter.size());}
    if(!fill)for(int i=0;i<(int)bs.size()&&!fill;i++)for(int j=i+1;j<(int)bs.size()&&!fill;j++)if(xorsets(bs[i],bs[j])==w)fill=2;
    string cat=to_string(r)+":rank"+to_string(4-lat.rank)+":torsion"+to_string(lat.torsion)+":fill"+to_string(fill)+":maxov"+to_string(maxov);counts[cat]++;
    out<<r<<'\t'<<4-lat.rank<<'\t'<<lat.torsion<<'\t'<<fill<<'\t'<<maxov<<'\t'<<lat.key()<<'\t';for(auto q:w)out<<q.first<<','<<sv(q.second)<<';';out<<'\t'<<gi<<','<<mask<<','<<pn<<'\n';
   }
  }

 }
 ofstream cc(root+"highrank_counts.tsv");for(auto[k,v]:counts){cout<<k<<'\t'<<v<<endl;cc<<k<<'\t'<<v<<endl;}
}
