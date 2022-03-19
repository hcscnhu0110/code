#include <bits/stdc++.h>
using namespace std;

int main(){
    string a,b;
    cin >> a;
    for(char& c: a) c = toupper(c);
    b=a;
    reverse(b.begin(), b.end());
    if(a==b) cout << "1\n";
    else cout << "0\n";
    return 0;
}
