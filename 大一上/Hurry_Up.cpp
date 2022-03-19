#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    string s;
    stringstream ss;
    while(getline(cin, s)){
        ss << "";
        ss.clear();
        int sum = 0;
        ss << s;
        //getline(ss,str,',');
        while(ss >> n) sum += n;
        cout << sum << "\n";
    }
    return 0;
}