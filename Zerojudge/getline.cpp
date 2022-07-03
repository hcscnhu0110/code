#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    getline(cin, s);
    stringstream ss;    //stringstream ss(s)
    ss << s;           
    string t;
    while(getline(ss, t, ' ')){
        cout << t << endl;
    }
}