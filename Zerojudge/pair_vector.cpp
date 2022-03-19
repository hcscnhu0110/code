#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    typedef vector< pair<int,int> > VP;
    VP vp;
    while(cin >> n >> m){
        vp.push_back(make_pair(n,m));

    }
    VP :: iterator it;
    for(it=vp.begin();it != vp.end();it++){
        cout << it -> first << " " << it -> second << endl;
    }
}