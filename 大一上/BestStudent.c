#include <stdio.h>

int main(){
    int x;
    int n=0;
    while(scanf("%d",&x) != EOF){
        n+=x;
    }
    printf("%d",n);
    return 0;
}