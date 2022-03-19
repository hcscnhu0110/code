#include <stdio.h>

int main(){
    int n,q;
    int c[510]={0};
    int i;
    int x,y;
    int a=0;
    int b=0;
    scanf("%d %d",&n,&q);
    for(i=0;i<q;i++){
        scanf("%d %d",&x,&y);
        a+=x;
        c[a]=y;
    }
    for(i=0;i<n;i++){
        b+=c[i];
    }
    printf("%d",b);
}