#include <bits/stdc++.h>
using namespace std;
int n, a, ans;

void DFS(int level, int Wnum, int Rnum, bool win){ 
    if(Wnum == a){ 
        ans++; 
        return;
    }

    if(Rnum == a) return; 
    
    if(win == 0) Wnum = 0; 
    if(win == 1) Rnum = 0; 

    if(level == n){ 
        if(n % 2 && Rnum) return; 
        ans++; 
        return;
    }
    DFS(level + 1, Wnum + 1, Rnum, 1); 
    DFS(level + 1, Wnum, Rnum + 1, 0); 
    return;
}

int main(){
    ios::sync_with_stdio(false); 
    cin.tie(0); 

    ans = 0; 

    cin >> n >> a;

    DFS(0, 0, 0, 0);

    cout << ans << "\n";
    return 0;
}