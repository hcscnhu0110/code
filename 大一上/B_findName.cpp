#include <bits/stdc++.h>
using namespace std;

struct table{
    string a, b;

};

int main(){
    table t[10000];
    int n, q;
    string num;
    cin >> n >> q;
    for(int i=0 ; i < n ; i++){
        cin >> t[i].a >> t[i].b;
    }
    for(int j=0 ; j < q ; j++){
        cin >> num;
        for(int i = 0; i < n; i++){
            if(num == t[i].b){
                cout << t[i].a << endl;
            }
        }
    }
    return 0;
}