// Independent exhaustive verifier: all 18-incidence pairings, no supplied graph list.
// Uses additive-potential union-find instead of a predetermined spanning tree.
// Full integer quotient coordinates from independent 4x4 diagonalization.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;
using I=int64_t;using V=array<I,4>;using Mat=array<V,4>;using Poly=set<V>;
V plusv(V a,const V&b,I s=1){for(int j=0;j<4;j++)a[j]+=s*b[j];return a;}
I minor3(const Mat&R,int a,int b,int c,int x,int y,int z){return R[a][x]*(R[b][y]*R[c][z]-R[b][z]*R[c][y])-R[a][y]*(R[b][x]*R[c][z]-R[b][z]*R[c][x])+R[a][z]*(R[b][x]*R[c][y]-R[b][y]*R[c][x]);}
V cross3(const Mat&R,int a,int b,int c){return {minor3(R,a,b,c,1,2,3),-minor3(R,a,b,c,0,2,3),minor3(R,a,b,c,0,1,3),-minor3(R,a,b,c,0,1,2)};}
I width(V w){return max(max({I(0),w[0],w[1]})-min({I(0),w[0],w[1]}),max({I(0),w[2],w[3]})-min({I(0),w[2],w[3]}));}
struct Group{
 Mat M,VV{};array<I,4>D{};int rank=0;I tor=1;
 Group(Mat R):M(R){
  for(int i=0;i<4;i++)VV[i][i]=1;
  auto swapcol=[&](int a,int b){for(Mat*P:{&M,&VV})for(auto&r:*P)swap(r[a],r[b]);};
  auto addcol=[&](int j,int k,I q){for(Mat*P:{&M,&VV})for(auto&r:*P)r[j]-=q*r[k];};
  for(int k=0;k<4;k++){
   int mi=-1,mj=-1;I best=INT64_MAX;
   for(int i=k;i<4;i++)for(int j=k;j<4;j++)if(M[i][j]&&abs(M[i][j])<best){best=abs(M[i][j]);mi=i;mj=j;}
   if(mi<0)break;swap(M[k],M[mi]);swapcol(k,mj);
   while(true){bool again=false;
    for(int i=k+1;i<4;i++)if(M[i][k]){
     I q=M[i][k]/M[k][k];for(int j=0;j<4;j++)M[i][j]-=q*M[k][j];
     if(M[i][k]){swap(M[k],M[i]);again=true;break;}}
    if(again)continue;
    for(int j=k+1;j<4;j++)if(M[k][j]){
     I q=M[k][j]/M[k][k];addcol(j,k,q);
     if(M[k][j]){swapcol(k,j);again=true;break;}}
    if(!again)break;
   }
   if(M[k][k]<0)for(I&v:M[k])v=-v;
   D[k]=M[k][k];tor*=D[k];++rank;
  }
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(i!=j&&M[i][j])throw string("diagonalization");
  for(auto row:R)if(red(row)!=V{})throw string("relation reduction");
 }
 I residue(I x,int j)const{if(j>=rank)return x;x%=D[j];return x<0?x+D[j]:x;}
 V red(V x)const{V y{};for(int j=0;j<4;j++){for(int i=0;i<4;i++)y[j]+=x[i]*VV[i][j];y[j]=residue(y[j],j);}return y;}
 V add(V a,V b)const{for(int j=0;j<4;j++)a[j]=residue(a[j]+b[j],j);return a;}
 V sub(V a,V b)const{for(int j=0;j<4;j++)a[j]=residue(a[j]-b[j],j);return a;}
 V scale(V a,I s)const{for(int j=0;j<4;j++)a[j]=residue(a[j]*s,j);return a;}
 bool order2(V a)const{return a!=V{}&&scale(a,2)==V{};}
 bool finite(V a)const{for(int j=rank;j<4;j++)if(a[j])return false;return true;}
 Poly shift(const Poly&P,V a)const{Poly Q;for(V b:P)Q.insert(add(a,b));return Q;}
 Poly power(const Poly&P,I k)const{Poly Q;for(V a:P){a=scale(a,k);if(Q.count(a))Q.erase(a);else Q.insert(a);}return Q;}
 bool equiv(const Poly&P,const Poly&Q)const{for(V a:P)if(shift(P,sub(*Q.begin(),a))==Q)return true;return false;}
 bool free_equiv(const Poly&P,const Poly&Q)const{
  Poly PP,QQ;for(V a:P){for(int j=0;j<rank;j++)a[j]=0;PP.insert(a);}for(V a:Q){for(int j=0;j<rank;j++)a[j]=0;QQ.insert(a);}
  if(PP.size()!=3||QQ.size()!=3)return false;
  for(V a:PP){V s=plusv(*QQ.begin(),a,-1);Poly z;for(V b:PP)z.insert(plusv(b,s));if(z==QQ)return true;}return false;
 }
 Poly mul(const Poly&P,const Poly&Q)const{Poly W;for(V a:P)for(V b:Q){V z=add(a,b);if(W.count(z))W.erase(z);else W.insert(z);}return W;}
};
struct Stats{I connected=0,finite_count=0,strip_count=0,high_count=0,maxorder=0,maxstrip=0;map<string,I>cases;};
array<Stats,3>stats;array<int,3>NAS={5,4,3};I leaves=0;array<pair<int,int>,9>pairs;array<int,18>partners;
void fail(string s,int na,const Mat&R){cerr<<"FAIL "<<s<<" na="<<na<<'\n';for(auto r:R){for(I x:r)cerr<<x<<' ';cerr<<'\n';}for(auto[a,b]:pairs)cerr<<a<<','<<b<<' ';cerr<<'\n';exit(7);}
void classify(int idx){
 int na=NAS[idx];Stats&st=stats[idx];
 array<int,6>parent;for(int i=0;i<6;i++)parent[i]=i;array<V,6>dist{};
 auto find=[&](int v){int root=v;V d{};while(parent[root]!=root){d=plusv(d,dist[root]);root=parent[root];}return pair<int,V>{root,d};};
 auto term=[&](int port){V r{};int v=port/3,c=port%3;if(c)r[(v<na?0:2)+c-1]=1;return r;};
 Mat R{};int nr=0;
 for(auto[a,b]:pairs){int va=a/3,vb=b/3;auto[ra,da]=find(va);auto[rb,db]=find(vb);
  V rel=plusv(plusv(plusv(da,term(a)),db,-1),term(b),-1);
  if(ra==rb){if(nr>=4)return;R[nr++]=rel;}
  else{parent[rb]=ra;dist[rb]=rel;}
 }
 if(nr!=4)return;
 auto[r0,d0]=find(0);array<V,6>positions{};
 for(int v=0;v<6;v++){auto[r,d]=find(v);if(r!=r0)return;positions[v]=plusv(d,d0,-1);}
 ++st.connected;
 V c0=cross3(R,1,2,3);I det=0;for(int j=0;j<4;j++)det+=R[0][j]*c0[j];
 if(det){++st.finite_count;st.maxorder=max(st.maxorder,abs(det));if(abs(det)>27)fail("finite order",na,R);return;}
 I T=0;V first{};I content=0;
 for(int a=0;a<2;a++)for(int b=a+1;b<3;b++)for(int c=b+1;c<4;c++){
  V w=cross3(R,a,b,c);I g=0;for(I x:w){T=gcd(T,abs(x));g=gcd(g,abs(x));}
  if(g&&!content){first=w;content=g;}
 }
 if(T){++st.strip_count;for(I&x:first)x/=content;I tr=T*width(first);st.maxstrip=max(st.maxstrip,tr);if(tr>14)fail("strip parameter",na,R);return;}
 ++st.high_count;Group G(R);Poly A,B;A.insert(V{});B.insert(V{});for(int j=0;j<4;j++){V e{};e[j]=1;(j<2?A:B).insert(G.red(e));}
 if(A.size()!=3||B.size()!=3){++st.cases["invalid_terms"];return;}
 array<Poly,6>columns;array<V,6>pos;vector<V>checks;
 for(int i=0;i<6;i++){pos[i]=G.red(positions[i]);columns[i]=G.shift(i<na?A:B,pos[i]);for(V q:columns[i])checks.push_back(q);}
 sort(checks.begin(),checks.end());checks.erase(unique(checks.begin(),checks.end()),checks.end());
 array<unsigned,6>bits{};unsigned total=0;for(int i=0;i<6;i++){for(V x:columns[i])bits[i]^=1U<<(lower_bound(checks.begin(),checks.end(),x)-checks.begin());total^=bits[i];}
 if(total)fail("cycle",na,R);
 array<unsigned,18>bas{};int crank=0;for(unsigned x:bits)while(x){int p=31-__builtin_clz(x);if(bas[p])x^=bas[p];else{bas[p]=x;++crank;break;}}
 if(crank!=5){++st.cases["not_circuit"];return;}
 Poly U,VV;for(int i=0;i<6;i++)(i<na?U:VV).insert(pos[i]);
 for(V u:U)for(V b:B){V h=G.sub(u,b);if(G.shift(B,h)==U&&G.shift(A,h)==VV){++st.cases["one_boundary"];return;}}
 for(const Poly*P:{&A,&B})for(V a:*P)for(V b:*P)if(G.order2(G.sub(a,b))){++st.cases["unit"];return;}
 // Direct finite-support certificate, not a rational-rank guess.
 for(const Poly*P:{&A,&B}){bool finite=true;for(V a:*P)finite&=G.finite(a);if(finite){if(G.tor>3)fail("finite polynomial order",na,R);++st.cases["finite_polynomial"];return;}}
 // Explicit sums of two boundaries.
 set<V>hc;for(V v:VV)for(V a:A)hc.insert(G.sub(v,a));
 for(auto i=hc.begin();i!=hc.end();++i)for(auto j=next(i);j!=hc.end();++j){Poly h={*i,*j};if(G.mul(B,h)==U&&G.mul(A,h)==VV){++st.cases["two_boundaries"];return;}}
 // Frobenius-square / single-involution identities in the full group.
 if(G.equiv(G.power(A,2),B)||G.equiv(G.power(B,2),A)){++st.cases["square"];return;}
 for(V a:A)for(V b:B){Poly B1=G.shift(B,G.sub(a,b));Poly p,q;set_difference(A.begin(),A.end(),B1.begin(),B1.end(),inserter(p,p.end()));set_difference(B1.begin(),B1.end(),A.begin(),A.end(),inserter(q,q.end()));if(p.size()==1&&q.size()==1&&G.order2(G.sub(*p.begin(),*q.begin()))){++st.cases["involution"];return;}}
 if(G.tor==3){
  V h{};bool ok=false;for(int j=0;j<G.rank;j++)if(G.D[j]==3){h[j]=1;ok=true;}
  if(!ok)fail("torsion-three coordinate",na,R);Poly norm={V{},h,G.scale(h,2)};
  for(V z:hc){Poly f=G.shift(norm,z);if(G.mul(B,f)==U&&G.mul(A,f)==VV){++st.cases["three_boundaries"];return;}}
  if(G.free_equiv(A,B)&&G.shift(U,h)==U&&G.shift(VV,h)==VV){++st.cases["odd_three_twist"];return;}
 }
 bool two=true;for(I d:G.D)if(d>2)two=false;
 if(G.tor==4&&two){
  for(V a:A)for(V b:B){V shift=G.sub(a,b);Poly B1=G.shift(B,shift);if(G.power(A,2)!=G.power(B1,2))continue;Poly U1=G.shift(U,shift);
   for(V u:U1)for(V aa:A){V h=G.sub(u,aa);if(G.shift(A,h)==U1&&G.shift(B1,h)==VV){++st.cases["double_involution"];return;}}
  }
 }
 fail("unclassified",na,R);
}
void visit(unsigned remaining,int depth){
 if(!remaining){++leaves;for(int i=0;i<3;i++)classify(i);return;}
 int a=__builtin_ctz(remaining);remaining^=1U<<a;unsigned cand=remaining;
 while(cand){int b=__builtin_ctz(cand);cand^=1U<<b;if(a/3==b/3)continue;pairs[depth]={a,b};visit(remaining^(1U<<b),depth+1);}
}
int main(){auto start=chrono::steady_clock::now();visit((1U<<18)-1,0);
 cout<<"{\"pairings_per_support_type\":"<<leaves<<",\"support_types\":[";
 for(int i=0;i<3;i++){if(i)cout<<',';auto&s=stats[i];cout<<"{\"A_columns\":"<<NAS[i]<<",\"connected\":"<<s.connected<<",\"rank_zero\":"<<s.finite_count<<",\"rank_one\":"<<s.strip_count<<",\"higher_rank\":"<<s.high_count<<",\"max_finite_order\":"<<s.maxorder<<",\"max_torsion_times_range\":"<<s.maxstrip<<",\"cases\":{";bool comma=false;for(auto&[k,v]:s.cases){if(comma)cout<<',';cout<<'\"'<<k<<"\":"<<v;comma=true;}cout<<"}}";}
 cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
