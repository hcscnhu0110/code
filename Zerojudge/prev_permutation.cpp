#include <bits/stdc++.h>
using namespace std;

//找出N個數字的所有排列

int main(){
    int n;
    while(cin >> n){
        int ans[n];
        int N=n;
        for(int i=0;i<n;i++){
            ans[i]=N;
            N--;
        }
        
        do{
            for(int i=0;i<n;i++){
                cout << ans[i] << " ";
            }
            cout << endl;
        }while(prev_permutation(ans,ans+n)); //陣列中數字如果由大到小存，用prev
    }
}