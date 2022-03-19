#include <stdio.h>


void solve(int n,int pivot,int ans[]){
    int flag;

    ans[pivot]=n+1;
    while(ans[pivot] > 1){
        flag=0;
        ans[pivot]-=1;
        for(int i=0;i<pivot;i++){
            if(ans[pivot] == ans[i]){
                flag=1;
                break;
            }
        }
        if(!flag){
            if(pivot+1 < n){
                solve(n,pivot+1,ans);
            }
            else{
                for(int i=0;i<n;i++){
                    printf("%d",ans[i]);
                }
                printf("\n");
            }    
        }
    } 
    
}

int main(){
    int n;

    while(scanf("%d",&n) != EOF){
        int ans[n];
        solve(n,0,ans);
    }
}