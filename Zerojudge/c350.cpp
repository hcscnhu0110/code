#include <bits/stdc++.h>
using namespace std;

void solve(int n, int k, int w, int* sum, int extra){
    if(n >= k){
        extra = n % k;
        n = (n / k) * w;
        *sum += n;
        if(extra){
            n += extra;
            extra = 0;
        }
        solve(n, k, w, sum, extra);
    }
}

int main(){
    int n, k, w;
    cin >> n >> k >> w;
    int sum = n;
    int extra;
    solve(n, k, w, &sum, extra);
    cout << sum;
}