#include <bits/stdc++.h>
using namespace std;

struct table{
    string a;
    int b,c,d;
};

int main(){
    table t[10000];
    int n;
    int score1=0,score2=0,score3=0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> t[i].a >> t[i].b >> t[i].c >> t[i].d;
    }
    for(int i=0;i<n;i++){
        if(t[i].b>score1){
            score1 = t[i].b;
        }
    }
    for(int i=0;i<n;i++){
        if(t[i].c>score2){
            score2 = t[i].c;
        }
    }
    for(int i=0;i<n;i++){
        if(t[i].d>score3){
            score3 = t[i].d;
        }
    } 
    
    return 0;
}