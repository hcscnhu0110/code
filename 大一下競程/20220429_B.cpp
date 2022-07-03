#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin >> n >> m;
    pair<int,int> p[10];
    for(int i=0;i<n;i++){
        int w,v;
        cin >> w >> v;
        p[i] = make_pair(w,v);
    }
    for(int i=0;i<n;i++){
        cout << p[i].first << " " << p[i].second << endl;
    }
}
