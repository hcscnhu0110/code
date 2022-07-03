#include <stdio.h>

int main(){
    int n;
    int ans[100];
    int count=0;

    while(scanf("%d",&n) != EOF){
        int N=n;
        while(N != 1){
            N=N/2;
            count++;
        }
        for(int i=count;i>=0;i--){
            ans[i]=n%2;
            n=n/2;
        }
        for(int i=0;i<=count;i++){
            printf("%d",ans[i]);
        }
        count=0;
        printf("\n");
    }
}