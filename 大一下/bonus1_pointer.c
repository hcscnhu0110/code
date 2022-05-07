#include <stdio.h>
#include <string.h>

void check(char *map,int *num,int i,int j,int n,int m){
    if(*(map + i*m + (j+1)) == '.' && *(num + i*m + (j+1)) != 1){
        *(num + i*m + (j+1)) += 1;
        check((char *)map,(int *)num,i,j+1,n,m);
    }
    if(*(map + i*m + (j-1)) == '.' && *(num + i*m + (j-1)) != 1){
        *(num + i*m + (j-1)) += 1;
        check((char *)map,(int *)num,i,j-1,n,m);
    }
    if(*(map + (i+1)*m + j) == '.' && *(num + (i+1)*m + j) != 1){
        *(num + (i+1)*m + j) += 1;
        check((char *)map,(int *)num,i+1,j,n,m);
    }
    if(*(map + (i-1)*m + j) == '.' && *(num + (i-1)*m + j) != 1){
        *(num + (i-1)*m + j) += 1;
        check((char *)map,(int *)num,i-1,j,n,m);
    }
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    char map[n][m];
    int num[n][m];
    int count = 0;
    memset(num,0,sizeof(num));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf(" %c",&map[i][j]);
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(map[i][j] == '.' && num[i][j] != 1){
                num[i][j] += 1;
                check((char *)map,(int *)num,i,j,n,m);
                count++;
            }
        }
    }
    printf("%d",count);
}
