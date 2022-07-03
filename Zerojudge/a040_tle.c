#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int search(char a[],int lens){
    int count=0;
    for(int i=0;i<lens;i++){
        if(a[i]=='0'){
            count++;
        }
    }
    return count;
}

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
    int lens0,lens;
    int* arr;
    int result=0;

    while(scanf("%d",&n) != EOF){
        int count=0;
        scanf("%d",&m);
        for(int i=n;i<=m;i++){
            sprintf(a,"%d",i);
            lens0=strlen(a);
            lens=lens0-search(a,lens0);
            arr=trans(i,lens);
            for(int j=0;j<lens;j++){
                result+=pow(arr[j],lens0);
            }
            if(result == i){
                printf("%d ",i);
                count++;
            }
            result=0;
            free(arr);
            memset(a,0,sizeof(a));
        }
        if(count==0){
            printf("none");
        }
        printf("\n");
    
    }
    return 0;
}