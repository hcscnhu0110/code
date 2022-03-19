#include <bits/stdc++.h>
using namespace std;


bool compare(pair<int,int> a,pair<int,int> b){
    if(a.second == b.second){
        return a.first < b.first;
    }
    else{
        return a.second > b.second;
    }
}


int main(){
    int n,m;
    int num,money;

    ios :: sync_with_stdio(false);
    cin.tie(0);
    
    cin >> n >> m;
    vector<int> v(n,0);
    pair<int,int> ans[n];

    for(int i=0;i<m;i++){
        cin >> num >> money;
        v[num] += money;
    }
    for(int i=0;i<n;i++){
        ans[i] = make_pair(i,v[i]);
    }
    sort(ans,ans+n,compare);
    for(int i=0;i<n;i++){
        cout << ans[i].first << " " << ans[i].second << endl;
    }

}