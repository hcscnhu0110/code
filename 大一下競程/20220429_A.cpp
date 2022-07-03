#include <bits/stdc++.h>
using namespace std;

int main(){

    ios :: sync_with_stdio(false);
    cin.tie(0);

    int n,q;
    cin >> n >> q;
    int num[n+1] = {0};
    int input;
    int k = 1;
    for(int i=0;i<n;i++){
        cin >> input;
        num[k] += num[k-1] + input; 
        k++;
    }
    int l,r;
    for(int i=0;i<q;i++){
        cin >> l >> r; 
        cout << num[r] - num[l-1] << endl;
    }
}