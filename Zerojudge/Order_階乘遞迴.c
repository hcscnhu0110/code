#include <stdio.h>

int factorial(int n){
    if(n == 0){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}

int main(){
    int n;
    
    while(scanf("%d",&n) != EOF){
        if(n == 0){
            printf("0! = 1 = 1\n");
        }
        else{
            printf("%d! = ",n);
            for(int i=n;i>=2;i--){
                printf("%d * ",i);
            }
            printf("1 = %d\n",factorial(n));
        }
    }
    return 0;
}