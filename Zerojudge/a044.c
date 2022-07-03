#include <stdio.h>

int factorial(int n){
    int x=2;
    int ans=0;
    if(n == 2){
        return 2;
    }
    else{
        return (n-1)+factorial(n-1);
    }
}

int main(){
    int n;
    int ans=0;
    while(scanf("%d",&n) != EOF){
        for(int i=n;i>=2;i--){
            ans+=factorial(i);
        }
        printf("%d\n",ans+2);
        ans=0;
    }
    return 0;
}