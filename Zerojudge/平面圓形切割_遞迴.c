#include <stdio.h>

int factorial(int n){
    if(n==1){
        return 2;
    }
    else{
        return ((n-1)*2)+factorial(n-1);
    }
}

int main(){
    int n;
    int ans;
    while(scanf("%d",&n) != EOF){
        ans=factorial(n);
        printf("%d\n",ans);
    }
    return 0;
}