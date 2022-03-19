#include <bits/stdc++.h>
using namespace std;

//找出N個數字的所有排列

int main(){
    int n;
    while(cin >> n){
        int ans[n];
        int k=1;
        for(int i=0;i<n;i++){
            ans[i]=k;
            k++;
        }
        
        do{
            for(int i=0;i<n;i++){
                cout << ans[i] << " ";
            }
            cout << endl;
        }while(next_permutation(ans,ans+n)); //陣列中數字如果由小到大存，用next
    }
}