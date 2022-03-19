#include <stdio.h>

int main(){
    int x,y;
    int a[5]={0},b[5]={0};
    int i;
    scanf("%d%d",&x,&y);
    for(i=4;i>=0;i--){
        a[i]=x%2;
        b[i]=y%2;
        x=x/2;
        y=y/2;
    }
    for(i=0;i<=4;i++){
        printf("%d",a[i]);
        printf("%d",b[i]);
    }
    return 0;
}