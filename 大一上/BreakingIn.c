#include <stdio.h>

int N[510][510],M[510][510],O[510][510];


int main(){
    int n,m,r;
    int a,b;
    scanf("%d %d %d",&n,&m,&r);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d",&a);
            N[i][j]+=a;
        }
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<r;j++){
            scanf("%d",&b);
            M[i][j]+=b;
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<r;j++){
            for(int k=0;k<m;k++){
                O[i][j]+=N[i][k]*M[k][j];
            }
            printf("%d ",O[i][j]);  
        }
        printf("\n");
    }
    return 0;
}