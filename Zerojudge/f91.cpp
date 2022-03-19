#include <bits/stdc++.h>
using namespace std;

int factorial(int n){
    if(n >= 101){
        return n-10;
    }
    else if(n <= 100){
        return factorial(factorial(n+11));
    }
    return 0;
}

int main(){
    int n;
    while(1){
        cin >> n;
        if(n == 0){
            break;
        }
        else{
            cout << "f91(" << n << ") = " << factorial(n) << endl;
        }
    }
    return 0;
}