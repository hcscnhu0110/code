#include <stdio.h>

long long int abc(long long int a,long long int b){
    return a+b;
}

long long int def(long long int a,long long int b){
    return a-b;
}

long long int ghi(long long int a,long long int b){
    return a*b;
}

int main(){
    char c;
    int x,y;
    while(scanf(" %c%d%d",&c,&x,&y) != EOF){
        if(c=='+'){
            long long int result=abc(x,y);
            printf("%lld\n",result);
        }
        if(c=='-'){
            long long int result=def(x,y);
            printf("%lld\n",result);
        }
        if(c=='*'){
            long long int result=ghi(x,y);
            printf("%lld\n",result);
        }
    } 
    return 0;
}