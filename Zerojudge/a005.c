#include <stdio.h>

int main(){
    int t;
    int a[10];
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        for(int j=0;j<4;j++){
            scanf("%d",&a[j]);
        }
        if(a[1]-a[0]==a[2]-a[1]){
            a[4]=a[3]+(a[1]-a[0]);
            printf("%d %d %d %d %d\n",a[0],a[1],a[2],a[3],a[4]);
        }
        else if(a[1]/a[0]==a[2]/a[1]){
            a[4]=a[3]*(a[1]/a[0]);
            printf("%d %d %d %d %d\n",a[0],a[1],a[2],a[3],a[4]);
        }
    }
    return 0;
}