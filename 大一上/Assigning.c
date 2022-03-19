#include <stdio.h>

int main(){
    int n,q;
    int x,y;
    int a[510]={0};
    int tmp;
    scanf("%d %d",&n,&q);
    for(int i=0;i<n;i++){
        scanf("%d",&x);
        a[i]+=x;
    }
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                tmp=a[j];
                a[j]=a[j+1];
                a[j+1]=tmp;
            }
        }
    }
    for(int i=0;i<q;i++){
        scanf("%d",&y);
        for(int i=0;i<n;i++){
            if(y-1==i){
                printf("%d\n",a[i]);
            }
        }
    }
    return 0;
}