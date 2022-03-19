#include <stdio.h>

long long int mul(long long int n,long long int t){
    long long int T=t;
    if(n==1){
        return 1;
    }
    else{
        n=n-1;
        while(n > 1){
            t=t*T;
            n--;
        }
        return t;
    }
} 

int main(){
    long long int n,t;
    long long int a,x=0;
    long long int b[20],c[20];
    long long int ans=0;
    scanf("%lld %lld",&n,&t);
    int N=n;
    for(int i=n;i>=0;i--){
        scanf("%lld",&a);
        b[i]=a*x;
        x++;
    }
    for(int i=0;i<N;i++){
        c[i]=mul(n,t);
        n--;
    }
    for(int i=N-1;i>=0;i--){
        printf("%lld ",b[i]);
        ans+=b[i]*c[i];
    }
    printf("\n");
    printf("%lld\n",ans);
    return 0;
}