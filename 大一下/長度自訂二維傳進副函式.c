#include <stdio.h>
#include <string.h>

void aaa(int *c,int n,int m){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            *(c+i*m+j) += 1;      //i,j 就是二維陣列裡的座標
        }
    }
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int c[n][m];
    memset(c,0,sizeof(c));
    aaa((int*) c,n,m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("%d",c[i][j]);
        }
        printf("\n");
    }
}