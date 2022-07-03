#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input;
    while(cin >> n){
        vector<int> num;
        for(int i = 0; i < n; i++){
            cin >> input;
            num.push_back(input);
        }
        sort(num.begin(), num.end());
        for(auto &ans : num){
            cout << ans << " ";
        }
        cout << '\n';
    }
}