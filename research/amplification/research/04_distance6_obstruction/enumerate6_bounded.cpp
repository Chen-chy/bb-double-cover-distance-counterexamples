// Enumerate normalized incidence presentations of all six-column mixed cycles.
// Does not assume the cycle is nonboundary; admissibility is checked separately.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;
using V=array<int,4>;
V add(V a,const V&b,int s=1){for(int i=0;i<4;i++)a[i]+=s*b[i];return a;}
int det3(const array<V,4>&R,int a,int b,int c,int x,int y,int z){return R[a][x]*(R[b][y]*R[c][z]-R[b][z]*R[c][y])-R[a][y]*(R[b][x]*R[c][z]-R[b][z]*R[c][x])+R[a][z]*(R[b][x]*R[c][y]-R[b][y]*R[c][x]);}
int rank_small(const array<V,4>&R){
 for(int a=0;a<2;a++)for(int b=a+1;b<3;b++)for(int c=b+1;c<4;c++)
 for(int x=0;x<2;x++)for(int y=x+1;y<3;y++)for(int z=y+1;z<4;z++)if(det3(R,a,b,c,x,y,z))return 3;
 for(int a=0;a<3;a++)for(int b=a+1;b<4;b++)for(int x=0;x<3;x++)for(int y=x+1;y<4;y++)if(R[a][x]*R[b][y]!=R[a][y]*R[b][x])return 2;
 for(auto r:R) for(int x:r) if(x) return 1;
 return 0;
}
void printv(ostream&o,const V&v){o<<'[';for(int i=0;i<4;i++){if(i)o<<',';o<<v[i];}o<<']';}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: enumerate6_bounded graph_file output_jsonl\n";return 2;}
 ifstream in(argv[1]);ofstream out(argv[2]);
 if(!in||!out){cerr<<"cannot open input/output file\n";return 2;}
 int ng;in>>ng;vector<array<pair<int,int>,9>>graphs(ng);for(auto&g:graphs)for(auto&e:g)in>>e.first>>e.second;
 vector<array<int,3>>perms;array<int,3>p={0,1,2};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 for(int na:{5,4,3}){
  long total=0,low=0;array<long,4>counts{}; int maxdet4=0,maxwidth=0; long ranks3=0,ranks4=0;
  for(int gi=0;gi<ng;gi++){
   auto edges=graphs[gi];array<array<int,3>,6> inc{};array<int,6>deg{};
   for(int e=0;e<9;e++){auto[a,b]=edges[e];inc[a][deg[a]++]=e;inc[b][deg[b]++]=e;}
   // A fixed spanning tree and its traversal order.
   array<bool,6>seen{};seen[0]=true;vector<array<int,3>>tree;array<bool,9>istree{};
   while(tree.size()<5){bool added=false;for(int e=0;e<9;e++){auto[a,b]=edges[e];if(seen[a]!=seen[b]){if(!seen[a])swap(a,b);tree.push_back({a,b,e});seen[b]=true;istree[e]=true;added=true;}}if(!added&&tree.size()<5)return 3;}
   array<array<int,9>,6>slot{};for(int v=0;v<6;v++)for(int j=0;j<3;j++)slot[v][inc[v][j]]=j;
   vector<int>variable;for(int v=0;v<6;v++)if(v!=0&&v!=na)variable.push_back(v);
   for(int id=0;id<1296;id++){
    ++total;array<int,6>choice{};int q=id;for(int v:variable){choice[v]=q%6;q/=6;}
    array<array<V,9>,6>terms{};
    for(int v=0;v<6;v++)for(int e:inc[v]){int c=perms[choice[v]][slot[v][e]];if(c)terms[v][e][(v<na?0:2)+c-1]=1;}
    array<V,6>pos{};for(auto[a,b,e]:tree)pos[b]=add(add(pos[a],terms[a][e]),terms[b][e],-1);
    array<V,4>R{};int k=0;for(int e=0;e<9;e++)if(!istree[e]){auto[a,b]=edges[e];R[k++]=add(add(add(pos[a],terms[a][e]),pos[b],-1),terms[b][e],-1);}
    int rank=rank_small(R);++counts[rank];
    if(rank>=3){
      int det=R[0][0]*det3(R,1,2,3,1,2,3)-R[0][1]*det3(R,1,2,3,0,2,3)+R[0][2]*det3(R,1,2,3,0,1,3)-R[0][3]*det3(R,1,2,3,0,1,2);
      if(det){++ranks4;maxdet4=max(maxdet4,abs(det));}
      else{
       ++ranks3;int best=1000000;
       for(int a=0;a<2;a++)for(int b=a+1;b<3;b++)for(int c=b+1;c<4;c++){
        V w={det3(R,a,b,c,1,2,3),-det3(R,a,b,c,0,2,3),det3(R,a,b,c,0,1,3),-det3(R,a,b,c,0,1,2)};
        int rho=max(*max_element(w.begin(),w.begin()+2),0)-min(*min_element(w.begin(),w.begin()+2),0);
        rho=max(rho,max(*max_element(w.begin()+2,w.end()),0)-min(*min_element(w.begin()+2,w.end()),0));
        if(rho)best=min(best,rho);
       }
       if(best==1000000) return 4;
       maxwidth=max(maxwidth,best);
      }
      continue;
    }
    ++low;
    out<<"{\"na\":"<<na<<",\"graph\":"<<gi<<",\"labels\":[";for(int i=0;i<6;i++){if(i)out<<',';out<<choice[i];}out<<"],\"rank\":"<<rank<<",\"R\":[";
    for(int i=0;i<4;i++){if(i)out<<',';printv(out,R[i]);}out<<"],\"positions\":[";for(int i=0;i<6;i++){if(i)out<<',';printv(out,pos[i]);}out<<"]}\n";
   }
  }
  cerr<<"na="<<na<<" total="<<total<<" rank<=2="<<low<<" rank bins=";for(long c:counts)cerr<<c<<',';cerr<<" rank3="<<ranks3<<" rank4="<<ranks4<<" max finite order="<<maxdet4<<" max T*rho bound="<<maxwidth<<'\n';
 }
}
