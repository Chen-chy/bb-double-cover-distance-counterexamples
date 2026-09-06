// Exact search for non-boundary binary column-matroid circuits.
// Exhaustiveness: at an odd syndrome row, partition completions by their
// smallest still-available selected column on that row. Earlier columns
// are forbidden in each successive branch. Stop at the first closed cycle:
// every minimum non-boundary cycle has circuit support.
// Cyclic symmetry permits roots at left column 0, or right column 0 with
// all left columns forbidden. No timeouts or heuristic node cutoffs.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
constexpr int NW=16; // support <=1024; hence period L <=512
struct Bits {
 array<uint64_t,NW> x{};
 bool get(int i)const{return (x[i/64]>>(i%64))&1;}
 void set(int i){x[i/64]|=1ULL<<(i%64);}
 void flip(int i){x[i/64]^=1ULL<<(i%64);}
 void join(const Bits& b){for(int j=0;j<NW;j++)x[j]|=b.x[j];}
 Bits operator^(const Bits&b)const{Bits r;for(int j=0;j<NW;j++)r.x[j]=x[j]^b.x[j];return r;}
 bool empty()const{for(auto z:x)if(z)return false;return true;}
 int weight()const{int w=0;for(auto z:x)w+=__builtin_popcountll(z);return w;}
 int top()const{for(int j=NW-1;j>=0;j--)if(x[j])return 64*j+63-__builtin_clzll(x[j]);return -1;}
};
int L,n,lim;vector<int> ae,be;vector<Bits>cols,bas;vector<vector<int>> inc;
uint64_t nodes=0,closed=0,logical_count=0;bool stop_first=true,found=false;Bits witness;
bool nonboundary(Bits v){for(int p=n-1;p>=0;p--)if(v.get(p)){
 if(bas[p].empty()) return true;
 v=v^bas[p];}return false;}
void dfs(Bits support,Bits syndrome,Bits forbidden,int size){
 ++nodes;
 if(syndrome.empty()){
  ++closed;if(nonboundary(support)){logical_count++;witness=support;found=true;}
  return;
 }
 int left=lim-size;
 if(left<=0||syndrome.weight()>3*left)return;
 // Choose the odd row with fewest available incident columns.
 int row=-1, best=999;
 for(int r=0;r<L;r++)if(syndrome.get(r)){
  int count=0;for(int c:inc[r])if(!forbidden.get(c))count++;
  if(!count)return;
  if(count<best){best=count;row=r;if(best==1)break;}
 }
 // Each branch chooses the least column still used on this row.
 for(int c:inc[row])if(!forbidden.get(c)){
  forbidden.set(c);Bits ns=support;ns.set(c);
  dfs(ns,syndrome^cols[c],forbidden,size+1);
  if(found&&stop_first)return;
 }
}
int main(int argc,char**argv){
 if(argc!=9){cerr<<"usage: circuit_search L a0 a1 a2 b0 b1 b2 max_weight\n";return 2;}
 L=atoi(argv[1]);n=2*L;lim=atoi(argv[8]);if(L<=0||n>64*NW)return 2;
 for(int j=2;j<5;j++)ae.push_back(atoi(argv[j])%L);
 for(int j=5;j<8;j++)be.push_back(atoi(argv[j])%L);
 if(ae[0]==ae[1]||ae[0]==ae[2]||ae[1]==ae[2]||be[0]==be[1]||be[0]==be[2]||be[1]==be[2])return 2;
 cols.resize(n);inc.resize(L);bas.resize(n);
 for(int i=0;i<L;i++){
  for(int a:ae)cols[i].flip((i+a)%L);
  for(int b:be)cols[L+i].flip((i+b)%L);
  Bits v;for(int b:be)v.flip((i+b)%L);for(int a:ae)v.flip(L+(i+a)%L);
  while(!v.empty()){int p=v.top();if(bas[p].empty()){bas[p]=v;break;}v=v^bas[p];}
 }
 for(int c=0;c<n;c++)for(int r=0;r<L;r++)if(cols[c].get(r))inc[r].push_back(c);
 int rank=0;for(auto &v:bas)rank+=!v.empty();
 auto t0=chrono::steady_clock::now();
 for(int root: {0,L}){
  Bits s,f;s.set(root);f.set(root);
  if(root==L)for(int c=0;c<L;c++)f.set(c);
  dfs(s,cols[root],f,1);if(found&&stop_first)break;
 }
 double secs=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
 cout<<"{\"L\":"<<L<<",\"k\":"<<2*(L-rank)<<",\"max_weight\":"<<lim<<",\"found\":"<<(found?"true":"false")
 <<",\"nodes\":"<<nodes<<",\"closed_cycles\":"<<closed<<",\"seconds\":"<<secs;
 if(found){cout<<",\"weight\":"<<witness.weight()<<",\"u\":[";bool first=true;
 for(int i=0;i<L;i++)if(witness.get(i)){if(!first)cout<<",";cout<<i;first=false;}
 cout<<"],\"v\":[";first=true;
 for(int i=0;i<L;i++)if(witness.get(L+i)){if(!first)cout<<",";cout<<i;first=false;}
 cout<<"]";}
 cout<<"}\n";
}
