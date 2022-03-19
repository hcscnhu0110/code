#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input1,input2;
    vector<int> a(10000000,0);
    int ans=0;

    while(cin >> n){
        for(int i=0;i<n;i++){
            cin >> input1 >> input2;
            for(int j=input1;j<input2;j++){
                a[j] = 1;
            }
        }
        for(int i=0;i<a.size();i++){
            ans += a[i];
        }
        cout << ans << endl;
        ans=0;
    }
    return 0;
}