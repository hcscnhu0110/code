#include <stdio.h>

int main(){
    int n;
    int b[1010];
    int tmp=0;

    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&b[i]);
    }


    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(b[j]>b[j+1]){
                tmp=b[j+1];
                b[j+1]=b[j];
                b[j]=tmp;
            }
        }
    }
    printf("%d",b[n-1]-b[0]);
    return 0;
}