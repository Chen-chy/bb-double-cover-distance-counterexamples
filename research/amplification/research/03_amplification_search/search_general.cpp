// Exact binary BB nonboundary-circuit search on C_l x C_m.
// Protocol: l m ax0 ay0 ax1 ay1 ax2 ay2 bx0 by0 bx1 by1 bx2 by2 bound node_budget
// A zero node budget means no cutoff. A cutoff NEVER certifies exclusion.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
const uint64_t ORDER=getenv("BB_ORDER")?strtoull(getenv("BB_ORDER"),nullptr,10):0;
uint64_t hashv(uint64_t x){x+=ORDER*0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
constexpr int MAXM=512, MAXN=1024, W=16;
struct Bits{array<uint64_t,W> a{};void flip(int i){a[i>>6]^=uint64_t(1)<<(i&63);}bool get(int i)const{return(a[i>>6]>>(i&63))&1;}int top()const{for(int j=W-1;j>=0;--j)if(a[j])return 64*j+63-__builtin_clzll(a[j]);return -1;}void xorr(const Bits&b){for(int j=0;j<W;j++)a[j]^=b.a[j];}};
struct Search{
 int l,m,M,n,lim,k,depth=0,sw=0; uint64_t nodes=0,budget=0,closed=0;bool found=false,cutoff=false;
 array<vector<int>,MAXN> col;array<vector<int>,MAXM> inc;int maxweight=0;array<int,MAXM> avail{};
 array<unsigned char,MAXN> forbidden{};array<uint64_t,MAXM/64> syn{};
 vector<Bits> basis;vector<int> support,witness;
 int pos(int x,int y)const{x%=l;y%=m;if(x<0)x+=l;if(y<0)y+=m;return x*m+y;}
 Search(int ll,int mm,const vector<array<int,2>>&A,const vector<array<int,2>>&B):l(ll),m(mm),M(l*m),n(2*M),basis(n){
  if(l<=0||m<=0||M>MAXM)throw runtime_error("invalid size");
  for(int x=0;x<l;x++)for(int y=0;y<m;y++){
   int j=pos(x,y);for(auto a:A)col[j].push_back(pos(x+a[0],y+a[1]));for(auto b:B)col[M+j].push_back(pos(x+b[0],y+b[1]));
  }
  for(int c=0;c<n;c++){auto cc=col[c];sort(cc.begin(),cc.end());if(adjacent_find(cc.begin(),cc.end())!=cc.end())throw runtime_error("duplicate terms");maxweight=max(maxweight,int(cc.size()));for(int r:cc){inc[r].push_back(c);avail[r]++;}}
  for(int r=0;r<M;r++){if(avail[r]!=int(A.size()+B.size()))throw runtime_error("degree mismatch");if(ORDER)sort(inc[r].begin(),inc[r].end(),[](int a,int b){return hashv(a)<hashv(b);});}
  int rank=0;for(int j=0;j<M;j++){Bits v;for(int r:col[M+j])v.flip(r);for(int r:col[j])v.flip(M+r);
   while(true){int p=v.top();if(p<0)break;if(!basis[p].get(p)){basis[p]=v;rank++;break;}v.xorr(basis[p]);}}
  k=2*(M-rank);
 }
 bool logical(){Bits v;for(int c:support)v.flip(c);while(true){int p=v.top();if(p<0)return false;if(!basis[p].get(p))return true;v.xorr(basis[p]);}}
 void toggle(int c){for(int r:col[c]){uint64_t bit=uint64_t(1)<<(r&63);sw+=(syn[r>>6]&bit)?-1:1;syn[r>>6]^=bit;}}
 void ban(int c){forbidden[c]=1;for(int r:col[c])avail[r]--;}
 void unban(int c){forbidden[c]=0;for(int r:col[c])avail[r]++;}
 void dfs(){
  if(budget&&nodes>=budget){cutoff=true;return;}nodes++;
  if(!sw){closed++;if(logical()){found=true;witness=support;}return;}
  int left=lim-int(support.size());if(left<=0||sw>maxweight*left)return;
  // Packing odd rows with disjoint AVAILABLE column neighborhoods gives a
  // rigorous lower bound on the number of additional selected columns.
  if(sw>left){
   auto pending=syn;int packing=0;
   for(int j=0;j<(M+63)/64;j++)while(pending[j]){
    int r=64*j+__builtin_ctzll(pending[j]);
    if(++packing>left)return;
    pending[j]&=~(uint64_t(1)<<(r&63));
    for(int c:inc[r])if(!forbidden[c])for(int rr:col[c])pending[rr>>6]&=~(uint64_t(1)<<(rr&63));
   }
  }
  int best=100,row=-1;
  for(int j=0;j<(M+63)/64;j++){uint64_t b=syn[j];while(b){int r=64*j+__builtin_ctzll(b);b&=b-1;if(avail[r]<best||(ORDER&&avail[r]==best&&hashv(r)<hashv(row))){best=avail[r];row=r;if(best==0)return;}}}
  int banned[20],nb=0;
  for(int c:inc[row])if(!forbidden[c]){
   ban(c);banned[nb++]=c;support.push_back(c);toggle(c);dfs();toggle(c);support.pop_back();
   if(found||cutoff)break;
  }
  for(int j=nb-1;j>=0;j--)unban(banned[j]);
 }
 void run(int b,uint64_t cap){lim=b;budget=cap;nodes=closed=0;found=cutoff=false;witness.clear();if(!k)return;
  ban(0);support.push_back(0);toggle(0);dfs();toggle(0);support.pop_back();unban(0);
  if(found||cutoff)return;
  for(int c=0;c<M;c++)ban(c);
  ban(M);support.push_back(M);toggle(M);dfs();toggle(M);support.pop_back();unban(M);
  for(int c=0;c<M;c++)unban(c);
 }
};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int l,m,b,na,nb;uint64_t cap;
 while(cin>>l>>m>>na>>nb){vector<array<int,2>> A(na),B(nb);for(auto&a:A)cin>>a[0]>>a[1];for(auto&a:B)cin>>a[0]>>a[1];cin>>b>>cap;
  try{if(na+nb>20)throw runtime_error("too many terms");auto st=chrono::steady_clock::now();Search s(l,m,A,B);s.run(b,cap);double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();
   cout<<"{\"l\":"<<l<<",\"m\":"<<m<<",\"k\":"<<s.k<<",\"bound\":"<<b<<",\"found\":"<<(s.found?"true":"false")<<",\"cutoff\":"<<(s.cutoff?"true":"false")<<",\"nodes\":"<<s.nodes<<",\"closed\":"<<s.closed<<",\"seconds\":"<<sec<<",\"witness\":[";
   for(size_t j=0;j<s.witness.size();j++){if(j)cout<<',';cout<<s.witness[j];}cout<<"]}"<<endl;
  }catch(const exception&e){cout<<"{\"error\":\""<<e.what()<<"\"}"<<endl;}
 }
}
