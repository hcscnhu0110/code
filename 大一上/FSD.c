#include <stdio.h>

int main(){
    long long int n,m;
    long long int a[1010]={0},b[1010]={0};
    scanf("%lld %lld",&n,&m);
    for(int i=0;i<n;i++){
        scanf("%lld",&a[i]);
        b[(i+m)%n]=a[i];
    }
    for(int i=0;i<n;i++){
        printf("%lld ",b[i]);
    }
    return 0;
}