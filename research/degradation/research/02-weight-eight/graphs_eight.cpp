#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):8;
 vector<pair<int,int>> ps;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ps.push_back({i,j});
 vector<array<int,8>> perms;array<int,8> pp; iota(pp.begin(),pp.end(),0);do{perms.push_back(pp);}while(next_permutation(pp.begin(),pp.begin()+n));
 vector<vector<int>> inds;for(auto p:perms){vector<int> ind;for(auto [i,j]:ps){int u=min(p[i],p[j]),v=max(p[i],p[j]);int k=0;for(;k<(int)ps.size();k++)if(ps[k]==make_pair(u,v))break;ind.push_back(k);}inds.push_back(ind);}
 unordered_set<unsigned long long> seen; long long cnt=0; int types=0;vector<int>a(ps.size(),0),deg(n,3);
 ofstream out("graph_multiplicities_"+to_string(n)+".txt");ofstream autos("graph_auts_"+to_string(n)+".txt");
 auto code=[&](vector<int>const& x){unsigned long long u=0;for(int i=0;i<(int)x.size();i++)u|=((unsigned long long)x[i])<<(2*i);return u;};
 function<void(int)> dfs=[&](int k){
  if(k==(int)ps.size()){
   if(any_of(deg.begin(),deg.end(),[](int x){return x!=0;}))return;
   vector<int>vis(n,0);vis[0]=1;for(int z=0;z<n;z++)for(int j=0;j<(int)ps.size();j++)if(a[j]&&(vis[ps[j].first]||vis[ps[j].second]))vis[ps[j].first]=vis[ps[j].second]=1;
   if(count(vis.begin(),vis.end(),1)!=n)return;cnt++;
   auto c=code(a);if(seen.count(c))return;int gi=types++;
   for(int v:a)out<<v<<' ';out<<'\n';vector<int>aa(a.size());vector<int> aps;
   for(int j=0;j<(int)perms.size();j++){auto& ind=inds[j];for(int z=0;z<(int)a.size();z++)aa[z]=a[ind[z]];auto cc=code(aa);seen.insert(cc);if(cc==c)aps.push_back(j);}
   autos<<gi<<' '<<aps.size();for(int j:aps)for(int i=0;i<n;i++)autos<<' '<<perms[j][i];autos<<'\n';return;
  }
  auto [i,j]=ps[k];int lo=0,hi=min({2,deg[i],deg[j]});
  if(j==n-1)lo=hi=deg[i];
  if(hi>2||hi>deg[j]||lo>hi)return;
  for(int v=lo;v<=hi;v++){a[k]=v;deg[i]-=v;deg[j]-=v;
   bool ok=true;for(int u=i+1;u<n;u++){int rem=0;for(int z=k+1;z<(int)ps.size();z++)if(ps[z].first==u||ps[z].second==u)rem+=2;if(deg[u]>rem){ok=false;break;}}
   if(ok)dfs(k+1);deg[i]+=v;deg[j]+=v;
  }
 };
 dfs(0);cout<<"n="<<n<<" labelled="<<cnt<<" types="<<types<<" orbitset="<<seen.size()<<endl;
}
