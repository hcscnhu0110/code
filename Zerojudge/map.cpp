#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b=0;
    pair<int,int> p;
    typedef map<int,int> M;
    M m;
    while(cin >> p.first >> p.second){
        a = p.first;
        b = p.second;
        m.insert(make_pair(a,b));
    };
    M :: iterator it;
    for(it = m.begin();it != m.end();it++){
        cout << it -> first << " " << it -> second << endl; 
    }

    
}