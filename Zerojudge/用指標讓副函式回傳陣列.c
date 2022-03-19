#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//阿姆斯壯數測試

int* trans(int i,int lens){
    int r[10]={1000000,100000,10000,1000,100,10,1};
    int* arr=(int*)malloc(lens* sizeof(int));
    int k=0;
    for(int j=0;j<=6;j++){
        if(i/r[j]>=1){
            arr[k]=i/r[j];
            i=i%r[j];
            k++;
        }
    }
    return arr;
}

int main(){
    int n,m;
    char a[1000010];
    int lens;
    int* arr;
    while(scanf("%d",&n) != EOF){
            itoa(n,a,10);
            lens=strlen(a);
            arr=trans(n,lens);

        for(int i=0;i<lens;i++){
            printf("%d ",arr[i]);
        }
        printf("\n");
        free(arr);
    }
}