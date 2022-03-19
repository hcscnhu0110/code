#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input;
    vector<int> a; 
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> input;
        a.push_back(input);
    }
    for(int i=0;i<a.size();i++){
        cout << a.at(i) << " "; 
    }
}