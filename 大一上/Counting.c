#include <stdio.h>

int bs(int a[],int n,int y){
    int left=0,right=n,mid;
    while(left < right){
        mid = (left+right)/2;
        if(a[mid]<y){
            left=mid+1;
        }
        else if(a[mid]>y){
            right=mid;
        }
        else if(a[mid]==y){
            return 1;
        }
    }
    return -1;
}

int main(){
    int n,q;
    long long int x,y;
    int a[100010]={0};
    scanf("%d %d",&n,&q);
    for(int i=0;i<n;i++){
        scanf("%lld",&x);
        a[i]+=x;
    }
    for(int i=0;i<q;i++){
        scanf("%lld",&y);
        int result=bs(a,n,y);
        if(result == 1){
            printf("Yes\n");
        }
        else if(result == -1){
            printf("No\n");
        }
    }
    return 0;    
}