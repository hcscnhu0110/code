#include <stdio.h>

int main(){
    int n;
    int a=0;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        a+=i*i;
    }
    printf("%d",a);
    return 0;
}