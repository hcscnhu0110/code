#include <stdio.h>

int function(int a,int b,int i){
    if(i==1){
        return a;
    }
    if(i==2){
        return b;
    }
    if(i>=3 && i%2==1){
        return function(a,b,i-1)+function(a,b,i-2);
    }
    if(i>=3 && i%2==0){
        return (function(a,b,i-1))*2;
    }
}

int main(){
    int x,y;
    int i;
    scanf("%d %d %d",&x,&y,&i);
    int result=function(x,y,i);
    printf("%d",result);
    return 0;
}