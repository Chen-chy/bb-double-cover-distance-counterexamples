// Independent exact minimum-weight exclusion by equal-syndrome meet-in-the-middle.
// Used here for the length-78 reduced code; enumerates ALL subsets of size <=4.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
struct Word{uint64_t lo=0,hi=0;void flip(int j){if(j<64)lo^=1ULL<<j;else hi^=1ULL<<(j-64);}Word operator^(Word b)const{return{lo^b.lo,hi^b.hi};}int top()const{return hi?127-__builtin_clzll(hi):lo?63-__builtin_clzll(lo):-1;}};
struct Rec{uint64_t syn;Word w;};
int main(){const int L=39,n=78;vector<int>A={0,5,28},B={14,22,26,28};vector<uint64_t> cols(n);vector<Word>basis(n);
 for(int i=0;i<L;i++){for(int a:A)cols[i]^=1ULL<<((i+a)%L);for(int b:B)cols[L+i]^=1ULL<<((i+b)%L);Word v;for(int b:B)v.flip((i+b)%L);for(int a:A)v.flip(L+(i+a)%L);while(v.top()>=0){int p=v.top();if(basis[p].top()<0){basis[p]=v;break;}v=v^basis[p];}}
 auto nonboundary=[&](Word v){while(v.top()>=0){int p=v.top();if(basis[p].top()<0)return true;v=v^basis[p];}return false;};
 vector<Rec> rs;rs.reserve(1600000);rs.push_back({0,{}});
 for(int i=0;i<n;i++){Word a;a.flip(i);rs.push_back({cols[i],a});for(int j=i+1;j<n;j++){Word b=a;b.flip(j);uint64_t sj=cols[i]^cols[j];rs.push_back({sj,b});for(int k=j+1;k<n;k++){Word c=b;c.flip(k);uint64_t sk=sj^cols[k];rs.push_back({sk,c});for(int l=k+1;l<n;l++){Word d=c;d.flip(l);rs.push_back({sk^cols[l],d});}}}}
 sort(rs.begin(),rs.end(),[](const Rec&a,const Rec&b){return a.syn<b.syn;});uint64_t pairs=0,groups=0;set<pair<uint64_t,uint64_t>> cycles;
 for(size_t i=0;i<rs.size();){size_t j=i+1;while(j<rs.size()&&rs[j].syn==rs[i].syn)j++;if(j-i>1)groups++;
  for(size_t a=i;a<j;a++)for(size_t b=a+1;b<j;b++){pairs++;Word z=rs[a].w^rs[b].w;cycles.insert({z.lo,z.hi});if(__builtin_popcountll(z.lo)+__builtin_popcountll(z.hi)!=7){cerr<<"Unexpected short cycle weight\n";return 2;}if(nonboundary(z)){cerr<<"NONBOUNDARY FOUND\n";return 1;}}
  i=j;}
 cout<<"{\"L\":39,\"A\":[0,5,28],\"B\":[14,22,26,28],\"excluded_through_weight\":8,\"subset_records\":"<<rs.size()<<",\"equal_syndrome_pairs\":"<<pairs<<",\"collision_groups\":"<<groups<<",\"distinct_nonzero_cycles\":"<<cycles.size()<<",\"all_short_cycles_have_weight\":7,\"nonboundary_found\":false}"<<endl;
}
