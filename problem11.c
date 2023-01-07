#include <stdio.h>

int main(){
    int n, m;
    while(scanf("%d %d", &n, &m) != EOF){
        int matrix[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                scanf("%d", &matrix[i][j]);
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(j != n - 1){
                    printf("%d ", matrix[j][i]);
                }
                else{
                    printf("%d", matrix[j][i]);
                }
            }
            printf("\n");
        }
    }
}