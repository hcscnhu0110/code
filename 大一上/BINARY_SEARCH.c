#include <stdio.h>

long long int BS(long long int a[],int N,int x){
    int left=0,right=N,mid;
    while(left < right){
        mid=(left+right)/2;
        if(a[mid] < x){
            left=mid+1;
        }
        else if(a[mid] > x){
            right=mid;
        }
        else if(a[mid] = x){
            return mid+1;
        }
    }
    return -1;
}

int main(){
    int N;
    long long int a[100010];
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        scanf("%lld",&a[i]);
    }

    int M;
    int x;
    scanf("%d",&M);
    for(int i=0;i<M;i++){
        scanf("%d",&x);
        int result=BS(a,N,x);
        printf("%d\n",result);
    }
}