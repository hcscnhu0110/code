#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input;
    set<int> a;

    cin >> n;
    for(int i=0;i<n;i++){
        cin >> input;
        a.insert(input);
    }
    for(const auto &s : a){
        cout << s << " ";
    }

}