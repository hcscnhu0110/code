#include <stdio.h>

int main(){
    long long int a[200010]={0};
    long long int n;
    int i=0;
    while(scanf("%d",&n)){
        a[i]+=n;
        i+=1;
        if(n==-1){
            break;
        }
    }
    printf("%d",a[2]);
}