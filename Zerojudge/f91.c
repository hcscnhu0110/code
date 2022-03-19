#include <stdio.h>

int factorial(int n){
    if(n >= 101){
        return n-10;
    }
    else if(n <= 100){
        return factorial(factorial(n+11));
    }
}

int main(){
    int n;
    while(1){
        scanf("%d",&n);
        if(n == 0){
            break;
        }
        else{
            printf("f91(%d) = %d\n",n,factorial(n));
        }
    }
    return 0;
}