#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream f("date.in");
int n,m,x,y,dinxy[10][10],dinx[10],fin[10],start,nrf,ok;
string c,d[10][10][10];
void verif(int stare, string cuv, string stiva)
{
    if((cuv=="" || cuv=="l") && fin[stare]==1)
        {
            ok=1;
            return;
        }
    if(cuv=="")
        cuv="l";
    string lit1;
    lit1 = cuv[0];
    //cout<<lit1<<" ";
    for(int j=0;j<n;++j)
        for(int k=0;k<dinxy[stare][j];++k){
            string cuvant = d[stare][j][k];
            //cout<<cuvant<<" ";
            string litera;
            litera = cuvant[0];
            if(litera == lit1 || litera == "l"){
                //cout<<litera<<" ";
                string literastiva;
                literastiva = cuvant[2];
                //cout<<literastiva<<" ";
                string adaugstiva="";
                for(int i=4;i<cuvant.length();++i)
                    adaugstiva.push_back(cuvant[i]);
                // cout<<adaugstiva<<"\n";
                string primastiva;
                primastiva = stiva[0];
                //cout<<primastiva<<" "<<literastiva<<" ";
                if(primastiva == literastiva){
                    string stivacopy=stiva;
                    if(adaugstiva!="L")
                        stivacopy.erase(0,1);
                    if(adaugstiva!="E" && adaugstiva!="L")
                        stivacopy.insert(0,adaugstiva);
                    //cout<<stivacopy<<" ";
                    string cuvcopy=cuv;
                    if(litera != "l")
                        cuvcopy.erase(0,1);
                    //cout<<cuvcopy<<" ";
                    int starecopy=stare;
                    starecopy=j;
                    //cout<<starecopy<<" ";
                    verif(starecopy,cuvcopy,stivacopy);
                }
            }
        }

}
int main()
{
    for(int i=0;i<10;++i){
        for(int j=0;j<10;++j)
            dinxy[i][j]=0;
    }
    f >> n >> m;
    for(int i=0;i<m;++i){
        f >> x;
        f >> y;
        f >> c;
        d[x][y][dinxy[x][y]]=c;
        dinxy[x][y]++;
    }
    f >> start;
    f >> nrf;
    for(int i=0;i<n;++i)
        fin[i]=0;
    for(int i=0;i<nrf;++i){
        int x;
        f>>x;
        fin[x]=1;
    }
    string cuv;
    f >> cuv;
    string stiva,stiva2;
    stiva="Z";
    ok=0;
    verif(start,cuv,stiva);
    if(ok == 1)
        cout<<"ACCEPTAT";
    else
        cout<<"NU E ACCEPTAT";

    return 0;
}
