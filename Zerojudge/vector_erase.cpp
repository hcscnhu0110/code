#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v;
    int n;
    int input;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> input;
        v.push_back(input);
    }
    v.erase(v.begin()+1,v.begin()+3);
    v.insert(v.begin()+1,6);
    cout << v.size();

}