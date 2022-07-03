#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> a = {1, 2, 3, 4};
    vector<int> b = {9, 8, 7, 6, 4};
    a.swap(b);
    for(const auto &x : a){
        cout << x;
    }
}