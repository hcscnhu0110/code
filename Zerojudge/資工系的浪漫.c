#include <stdio.h>
#include <string.h>

int main(){
    int n,m;
    char c;
    long long int s,S;
    int count=0;

    scanf("%d %d",&n,&m);
    int graph[n][m];
    char result[100][100];
    memset(graph,0,sizeof(graph));
    //memset(result,'.',sizeof(result));
    scanf(" %c",&c);
    for(int i=0;i<n;i++){
        scanf("%lld",&s);
        S = s;
        while(S >= 1){
            S = S/2;
            count++;
        }
        for(int j=m-1;j>=m-count;j--){
            graph[i][j] = s%2;
            s = s/2;
        }
        count=0;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(graph[i][j] == 1){
                result[i][j] = c;
            }
            else if(graph[i][j] == 0){
                result[i][j] = '.';
            }
            printf("%c ",result[i][j]);
        }
        printf("\n");
    }
    return 0;
}