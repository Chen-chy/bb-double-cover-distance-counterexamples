#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 int r,m,cd;unsigned c;cin>>r>>m>>cd>>c;
 vector<int>d(r);vector<unsigned long long>G(r*m);vector<unsigned>lab(r);int D=0;
 for(int j=0;j<r;j++){cin>>d[j]>>lab[j];D+=d[j];for(int a=0;a<m;a++)cin>>G[j*m+a];}
 if(D+cd>27){cerr<<"too many states\n";return 3;}
 unsigned M=1u<<D,N=1u<<(D+cd); vector<uint8_t>out(M);
 vector<int>off(r);int t=0;for(int j=0;j<r;j++){off[j]=t;t+=d[j];}
 for(unsigned q=0;q<M;q++){
  unsigned o=0;
  for(int j=0;j<r;j++)for(int a=0;a<m;a++){
   auto mem=(q>>off[j])&((1u<<d[j])-1);o^=(__builtin_parityll(mem&(G[j*m+a]>>1))<<a);
  }out[q]=o;
 }
 vector<unsigned> nmem(M);
 for(unsigned q=0;q<M;q++){unsigned n=0;for(int j=0;j<r;j++)n|=(((q>>off[j])<<1)&((1u<<d[j])-1))<<off[j];nmem[q]=n;}
 int ib=1<<r;vector<unsigned>inmask(ib),outmask(ib),lmask(ib);
 for(int b=0;b<ib;b++)for(int j=0;j<r;j++)if(b>>j&1){inmask[b]|=1u<<off[j];lmask[b]^=lab[j];for(int a=0;a<m;a++)outmask[b]^=(G[j*m+a]&1)<<a;}
 vector<uint16_t>dist(N,65535);vector<unsigned>prev(N,UINT_MAX);vector<vector<unsigned>>buckets(1024);dist[0]=0;buckets[0].push_back(0);long long pops=0;unsigned goal=0;
 for(int cost=0;cost<1020;cost++){
  auto &bucket=buckets[cost];
  while(!bucket.empty()){
   unsigned q=bucket.back();bucket.pop_back();if(dist[q]!=cost)continue;pops++;
   auto mm=q&(M-1);auto ll=q>>D;
   if(mm==0 && ll){goal=q;cout<<"distance "<<cost<<" pops "<<pops<<" states "<<N<<"\n";goto done;}
   for(int b=0;b<ib;b++){
    unsigned l=ll^lmask[b];l=(l>>1)^((l&1)?(c>>1):0);
    unsigned v=(nmem[mm]|inmask[b])|(l<<D);int nc=cost+__builtin_popcount(out[mm]^outmask[b]);
    if(nc<dist[v]){dist[v]=nc;prev[v]=q;buckets[nc].push_back(v);}
   }
  }
 }
 done:
 if(!goal){cout<<"none\n";return 2;}
 if(argc>1){ofstream f(argv[1],ios::binary);for(unsigned i=0;i<N;i++){uint16_t v=min(dist[i],dist[goal]);f.write(reinterpret_cast<char*>(&v),sizeof(v));}}
 vector<unsigned>path;unsigned q=goal;
 while(q){path.push_back(q);q=prev[q];if(q==UINT_MAX){cerr<<"bad parent";return 4;}}
 reverse(path.begin(),path.end());cout<<"inputs ";for(auto v:path){unsigned b=0;for(int j=0;j<r;j++)b|=((v>>off[j])&1)<<j;cout<<b<<",";}cout<<"\n";
}
