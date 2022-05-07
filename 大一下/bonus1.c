#include <stdio.h>

char map[1010][1010];
int num[1010][1010];

void check(char map[][1010],int num[][1010],int i,int j,int n,int m){
    if(map[i][j+1] == '.' && num[i][j+1] != 1){
        num[i][j+1] += 1;
        check(map,num,i,j+1,n,m);
    }
    if(map[i][j-1] == '.' && num[i][j-1] != 1){
        num[i][j-1] += 1;
        check(map,num,i,j-1,n,m);
    }
    if(map[i+1][j] == '.' && num[i+1][j] != 1){
        num[i+1][j] += 1;
        check(map,num,i+1,j,n,m);
    }
    if(map[i-1][j] == '.' && num[i-1][j] != 1){
        num[i-1][j] += 1;
        check(map,num,i-1,j,n,m);
    }
}

int main(){
    int n,m;
    int count = 0;
    scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            scanf(" %c",&map[i][j]);
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(map[i][j] == '.' && num[i][j] != 1){
                num[i][j] += 1;
                check(map,num,i,j,n,m);
                count++;
            }
        }
    }
    printf("%d",count);
}