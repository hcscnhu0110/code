#include <stdio.h>

char map[1010][1010];
int num[1010][1010];

void check(char map[1010][1010],int num[1010][1010],int i,int j,int x_already,int y_already){
    int x_rec = x_already;
    int y_rec = y_already;
    if(map[i][j+1] == '.' && j+1 != y_rec && num[i][j+1] == 0){
        num[i][j+1] = num[i][j] + 1;
        x_already = i;
        y_already = j;
        check(map,num,i,j+1,x_already,y_already);
    }
    if(map[i][j-1] == '.' && j-1 != y_rec && num[i][j-1] == 0){
        num[i][j-1] = num[i][j] + 1;
        x_already = i;
        y_already = j;
        check(map,num,i,j-1,x_already,y_already);
    }
    
    if(map[i+1][j] == '.'  && i+1 != x_rec && num[i+1][j] == 0){
        num[i+1][j] = num[i][j] + 1;
        x_already = i;
        y_already = j;
        check(map,num,i+1,j,x_already,y_already);
    }
    if(map[i-1][j] == '.'  && i-1 != x_rec && num[i-1][j] == 0){
        num[i-1][j] = num[i][j] + 1;
        x_already = i;
        y_already = j;
        check(map,num,i-1,j,x_already,y_already);
    }
    if(map[i][j+1] == 'B'){
        num[i][j+1] = 1;
    }
    if(map[i][j-1] == 'B'){
        num[i][j-1] = 1;
    }
    if(map[i+1][j] == 'B'){
        num[i+1][j] = 1;
    }
    if(map[i-1][j] == 'B'){
        num[i-1][j] = 1;
    }
}

void cmp(int num[1010][1010],int bx,int by){
    int around[10]={0};
    int k = 0;
    if(num[bx][by+1] != 0){
        around[k] = num[bx][by+1];
        k++;
    }
    if(num[bx][by-1] != 0){
        around[k] = num[bx][by-1];
        k++;
    }
    if(num[bx+1][by] != 0){
        around[k] = num[bx+1][by];
        k++;
    }
    if(num[bx-1][by] != 0){
        around[k] = num[bx-1][by];
        k++;
    }

    int mini = around[0];
    for(int i=1;i<k;i++){
        if(around[i] > 0 && around[i] < mini){
            mini = around[i];
        }
    }
    printf("%d",mini);
}

int main(){
    int n,m;
    int ax = 0,ay = 0;
    int bx = 0,by = 0;
    scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            scanf(" %c",&map[i][j]);
            if(map[i][j] == 'A'){
                ax = i;
                ay = j;
            }
            else if(map[i][j] == 'B'){
                bx = i;
                by = j;
            }
        }
    }
    num[ax][ay] += 1;
    check(map,num,ax,ay,ax,ay);
    if(num[bx][by] == 0){
        printf("NO");
    }
    else if(num[bx][by] == 1){
        printf("Yes\n");
        cmp(num,bx,by);
    }
}