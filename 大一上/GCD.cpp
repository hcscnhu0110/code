#include <bits/stdc++.h>
using namespace std;

int GCD(int a, int b){
    return b? GCD(b, a % b) : a;
}

int main(){
    int a,b;
    cin >> a >> b;
    cout << GCD(a, b) << "\n";

    return 0;
}