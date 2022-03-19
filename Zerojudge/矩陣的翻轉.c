#include <stdio.h>

int main(){
    int a[110][110];
    int b[110][110];
    int n,m;
    
    while(scanf("%d",&n)!= EOF){
        scanf("%d",&m);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                scanf("%d",&a[i][j]);
                b[j][i]=a[i][j];
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                printf("%d ",b[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}