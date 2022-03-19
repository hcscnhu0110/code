#include <stdio.h>

int main(){
    int x,y,z=0;
    int a[5]={0},b[5]={0};
    int i;
    scanf("%d %d",&x,&y);
    for(i=4;i>=0;i--){
        a[i]=x%2;
        b[i]=y%2;
        if(x%2 !=0 && y%2 !=0){
            z++;
        }
        x=x/2;
        y=y/2;
    }
    printf("%d",z);
    return 0;
}