#include <stdio.h>

int main(){
    int N;
    int a[1010];
    int tmp;
    int count=0;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<N-1;i++){
        for(int j=0;j<N-i-1;j++){
            if(a[j]>a[j+1]){
                tmp=a[j];
                a[j]=a[j+1];
                a[j+1]=tmp;
                count+=1;
            }
        }
    }

    printf("%d",count);


}