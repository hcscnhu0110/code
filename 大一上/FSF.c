#include <stdio.h>

int main(){
    long long int a[100];
    long long int A;
    int b;
    int count=0;
    scanf("%lld %d",&A,&b);
    long long int num=A;
    while(A >= b){
        A=A/b;
        count++;
    }
    for(int i=count;i>=0;i--){
            a[i]=num%b;
            num=num/b;
    }
    for(int i=0;i<=count;i++){
        printf("%lld",a[i]);
    }
    return 0;
}