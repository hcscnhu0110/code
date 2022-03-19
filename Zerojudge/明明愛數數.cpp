#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    
    while(cin >> n >> m){
        int count = 0;
        int i = 1;
        int N=n;
        while(1){
            int x = N+i;
            count++;
            if(n+x > m){
                break;
            }
            else{
                n = n+x;
                i++;
            }
        }
        if(n > m){
            cout << count << endl;
        }
        else{
            cout << count+1 << endl;
        }
    }
}