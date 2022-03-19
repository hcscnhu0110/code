#include <stdio.h>

long long int bs(long long int a[],int n,long long int x){
    int y;
    long long int count=0;
    for(int i=0;i<n-1;i++){
        int left=i,right=n,mid;
        y=x-a[i];
        while(left < right-1){
            mid=(left+right)/2;
            if(a[mid]<y){
                left=mid;
            }
            else if(a[mid]>=y){
                right=mid;
            }
        }
        count+=n-right;
    }
    return count;
}

int main(){
    int n;
    long long int x;
    long long int a[300010];
    scanf("%d %lld",&n,&x);
    for(int i=0;i<n;i++){
        scanf("%lld",&a[i]);
    }
    long long int result=bs(a,n,x);
    printf("%lld\n",result);
    return 0;
}