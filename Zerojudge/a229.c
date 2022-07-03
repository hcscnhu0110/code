#include <stdio.h>

void solve(int n, int left, int right, int start){
    if(left < n){
        printf("(");  
        left++;
        solve(n, left, right, start);
    }
    else if(left == start){
        printf(")");
        right++;
    }
    if(left > right){
        solve(n, left, right, start);
    }
    else if(left == n && right == n){
        printf("\n");
        start--;
        left = 0;
        right = 0;
        solve(n, left, right, start);
    }
}

int main(){
    int n;
    scanf("%d",&n);
    int left = 0, right = 0;
    int start = n;
    solve(n, left, right, start);
}