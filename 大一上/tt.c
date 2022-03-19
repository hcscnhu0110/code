#include <stdio.h>

int mul(int n,int t){
    int T=t;
    if(n==1){
        return 1;
    }
    else{
        n=n-1;
        while(n > 1){
            t=t*T;
            n--;
        }
        return t;
    }
} 

int main(){
    int n,t;
    int a,x=0;
    int b[20],c[20];
    int ans=0;
    scanf("%d %d",&n,&t);
    int N=n;
    
    for(int i=0;i<N;i++){
        c[i]=mul(n,t);
        n--;
        printf("%d ",c[i]);
    }
    
}