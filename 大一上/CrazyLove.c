#include <stdio.h>

int isPrime(int n){
    if(n==1){
        return 2;
    }
    if(n==2){
        return 1;
    }
    int count=0;
    int a=0;
    if(n%2 != 0 && n>2){
        for(int i=2;i*i<=n;i++){
            a+=n%i;
            if(a == 0){
                return 2;
                count++;
            }
            a=0;
        }
        if(count==0){
        return 1;
        }
    }
    else{
        return 2;
    }
}

int main(){
    long long int n;
    int x;
    scanf("%lld",&n);
    for(int j=0;j<n;j++){
        scanf("%d",&x);
        int result=isPrime(x);
        if(result==1){
            printf("True\n");
        }
        else if(result==2){
            printf("False\n");
        }
    }
    return 0;
}