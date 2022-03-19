#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d %d",&b,&c);
    while(c){
        a=b;
        b=c;
        c=a%b;
    }
    printf("%d",b);
    return 0;
}