#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input;
    vector<int> a = {4,5,6};
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> input;
        a.insert(a.begin(),input);
    }
    a.insert(a.begin()+3,55);
    for(const auto &s : a){
        cout << s << " ";
    }

}