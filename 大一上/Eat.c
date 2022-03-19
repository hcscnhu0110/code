#include <stdio.h>

int main(){
    long long int n;
    long long int l,r;
    long long int a[200]={0};
    long long int b;
    long long int x;
    scanf("%lld",&n);
    for(int i=1;i<=n;i++){
        scanf("%lld",&x);
        a[i]+=x;
    } 
    while(scanf("%lld %lld",&l,&r) != EOF){
        b=0;                 //沒有在這裡歸0的話就會一直加到前一次的數值
        for(int i=l;i<=r;i++){
            b+=a[i];
        }
    printf("%lld ",b);
    }
    return 0;
}