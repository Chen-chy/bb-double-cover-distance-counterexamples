// Exact shortest terminated convolutional path and independently checkable closure certificate.
// A capped run is inconclusive. Only certified=true exports a lower-bound certificate.
// Stop with certified=true only when Dijkstra pops a nonzero compact-label return.
#include <cstdint>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <fstream>
#include <stdexcept>
using U=uint64_t;
struct Rec{uint16_t d;U parent;uint8_t input;};
int deg(U v){return v?63-__builtin_clzll(v):-1;}
U rem(U a,U b){while(deg(a)>=deg(b))a^=b<<(deg(a)-deg(b));return a;}
int main(int argc,char**argv){
 if(argc!=14){std::cerr<<"usage: mode A0 A1 B0 B1 E maxcost maxstates target kill label0 label1 certificate.bin\n";return 2;}
 int mode=atoi(argv[1]),sh=mode?2:1;
 U A0=strtoull(argv[2],0,0),A1=strtoull(argv[3],0,0),B0=strtoull(argv[4],0,0),B1=strtoull(argv[5],0,0),E=strtoull(argv[6],0,0);
 int limit=atoi(argv[7]);size_t cap=strtoull(argv[8],0,0); U targetpoly=strtoull(argv[9],0,0),killpoly=strtoull(argv[10],0,0);
 int D=std::max({deg(A0),deg(A1),deg(B0),deg(B1)}),e=deg(E),sb=sh*D;
 if(sb+e>=63||e<=0||D<1){std::cerr<<"capacity\n";return 2;}
 U mask=(U(1)<<sb)-1;
 auto inter=[&](U a,U b){if(!mode)return a;U out=0;for(int j=0;j<=D;j++){if(a>>j&1)out|=U(1)<<(2*j);if(b>>j&1)out|=U(1)<<(2*j+1);}return out;};
 U ac[4]={0,inter(A0,A1),inter(A1,A0),0},bc[4]={0,inter(B0,B1),inter(B1,B0),0};ac[3]=ac[1]^ac[2];bc[3]=bc[1]^bc[2];
 int lows=(1<<sh)-1,choices=1<<sh;
 if((ac[1]&lows)!=1 && (ac[1]&lows)!=2){std::cerr<<"A constant not monomial\n";return 2;}
 std::vector<unsigned>inv(1<<e);U iz=(E^1)>>1;
 for(unsigned j=0;j<inv.size();j++)inv[j]=(j>>1)^((j&1)?iz:0);
 std::vector<std::vector<U>> buckets(limit+1);buckets[0].push_back(0);
 std::unordered_map<U,Rec> seen;seen.reserve(std::min(cap,size_t(2000000)));seen.emplace(0,Rec{0,0,0});
 size_t popped=0;bool certified=false,capped=false;U goal=0;int best=-1;
 auto t0=std::chrono::steady_clock::now();
 for(int distance=0;distance<=limit && !certified&&!capped;distance++){
  auto &bucket=buckets[distance];
  for(size_t qi=0;qi<bucket.size();qi++){
   U state=bucket[qi];auto it=seen.find(state);if(it->second.d!=distance)continue;
   popped++;U syn=state&mask;unsigned label=state>>sb;
   if(syn==0 && rem(label,targetpoly)!=0 && rem(label,killpoly)==0){goal=state;best=distance;certified=true;break;}
   for(int v=0;v<choices;v++){
    int target=(syn^bc[v])&lows,u=0;
    for(int z=0;z<choices;z++)if((ac[z]&lows)==unsigned(target)){u=z;break;}
    int cost=__builtin_popcount(unsigned(v))+__builtin_popcount(unsigned(u));
    if(distance+cost>limit)continue;
    U ns=(syn^ac[u]^bc[v])>>sh;
    unsigned labeladd=0; if(v&1)labeladd^=strtoull(argv[11],0,0); if(v&2)labeladd^=strtoull(argv[12],0,0);
    unsigned nl=inv[label^labeladd];
    U key=ns|(U(nl)<<sb);
    auto old=seen.find(key);
    if(old!=seen.end()&&old->second.d<=distance+cost)continue;
    Rec val{uint16_t(distance+cost),state,uint8_t(v|(u<<sh))};
    if(old==seen.end()){if(seen.size()>=cap){capped=true;break;}seen.emplace(key,val);}else old->second=val;
    buckets[distance+cost].push_back(key);
   }
   if(capped)break;
  }
 }
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();
 std::cout<<"{\"certified\":"<<(certified?"true":"false")<<",\"capped\":"<<(capped?"true":"false")<<",\"D\":"<<D<<",\"distance\":"<<best<<",\"states\":"<<seen.size()<<",\"popped\":"<<popped<<",\"seconds\":"<<seconds;
 if(certified){std::vector<unsigned>path;U p=goal;while(p){auto r=seen.at(p);path.push_back(r.input);p=r.parent;}std::reverse(path.begin(),path.end());
  std::cout<<",\"physical\":[";for(int block=0;block<2;block++)for(int sheet=0;sheet<sh;sheet++){
   if(block||sheet)std::cout<<",";
   std::cout<<"[";bool comma=false;int shift=(block==0?sh:0)+sheet;
   for(size_t i=0;i<path.size();i++)if(path[i]>>shift&1){if(comma)std::cout<<",";std::cout<<i;comma=true;}
   std::cout<<"]";}
  std::cout<<"]";
  std::vector<std::pair<U,uint16_t>> cert;
  for(const auto &kv:seen)if(kv.second.d<best)cert.push_back({kv.first,kv.second.d});
  std::sort(cert.begin(),cert.end());
  std::ofstream out(argv[13],std::ios::binary);
  if(!out)throw std::runtime_error("Cannot write certificate");
  out.write("BBSL21C1",8);
  auto writele=[&](U x,int bytes){for(int i=0;i<bytes;i++){char c=char((x>>(8*i))&255);out.write(&c,1);}};
  writele(cert.size(),8);
  for(const auto &kv:cert){writele(kv.first,8);writele(kv.second,2);}
  std::cout<<",\"certificate_states\":"<<cert.size();
 }
 std::cout<<"}\n";
}
