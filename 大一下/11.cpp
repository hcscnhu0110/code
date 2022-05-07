#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v,v2;
    int input;
    for(int i=0;i<3;i++){
        cin >> input;
        v.push_back(input);
    }
    v2 = v;
    for(const auto  &s :v2){
        cout << s << " ";
    }    
}