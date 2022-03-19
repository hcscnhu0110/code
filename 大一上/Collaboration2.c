#include <stdio.h>
typedef long long lint;
lint n, a, ans;

void DFS(lint level, lint Wnum, lint Rnum, lint win, lint wt, lint rt){
    if(Rnum == a){
        ans++;
        return;
    }

    if(Wnum == a) return;
    
    if(level == n){
        if(rt < wt) return;
        ans++;
        return;
    }

    DFS(level + 1, 0, Rnum + 1, 1, wt, rt + 1);

    DFS(level + 1, Wnum + 1, 0, 0, wt + 1, rt);
    return;
}

int main(){
    ans = 0;
    scanf("%lld%lld", &n, &a);

    DFS(0, 0, 0, 2, 0, 0);

    printf("%lld", ans);
    return 0;
}