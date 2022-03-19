#include <stdio.h>

int main(){
    int n;
    while(1){
        scanf("%d",&n);
        if(n == 0){
            break;
        }
        for(int i=1;i<n;i++){
            if(i%7 == 0){
                continue;
            }
            else{
                printf("%d ",i);
            }
        }
        printf("\n");
    }
    return 0;
}