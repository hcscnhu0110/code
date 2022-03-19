#include <stdio.h>

int main(){
    int n,q;
    int x,y;
    int a[110]={0};
    scanf("%d %d",&n,&q);
    for(int i=0;i<n;i++){
        scanf("%d",&x);
        a[i]+=x;
    }
    for(int j=0;j<q;j++){
        scanf("%d",&y);
        printf("%d\n",a[y]);
    }
    return 0;
}