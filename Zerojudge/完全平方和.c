#include <stdio.h>
#include <math.h>

int search(int a,int b){
    int ans=0;
    for(int i=a;i<=b;i++){
        int x=sqrt(i);
        if(i/x == x && i%x == 0){
            ans+=i;
        }
    }
    return ans;
}

int main(){
    int t;
    int a,b;
    int ans;
    int k=1;

    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d %d",&a,&b);
        ans=search(a,b);
        printf("Case %d: %d\n",k,ans);
        k++;
    }
}