#include <bits/stdc++.h>
using namespace std;

int main(){
    pair<int,int> p;
    int n,m;
    while(cin >> n >> m){
        p = make_pair(n,m);
        cout << p.first << " " << p.second << endl;
    }
}