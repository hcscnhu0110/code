#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    string s;
    int lens;
    int result=0;
    
    while(cin >> n >> m){
        int count=0;
        for(int i=n;i<=m;i++){
            s=to_string(i);
            lens=s.length();
            for(int j=0;j<lens;j++){
                result+=pow(s[j]-'0',lens);
            }
            if(result == i){
                cout << i << " ";
                count++;
            }
            result=0;
        }
        if(count == 0){
            cout << "none" ;
        }
        cout << endl;
    }
    
}