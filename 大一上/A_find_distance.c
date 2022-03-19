#include <stdio.h>

int ans[1000000];


int main(){
    int n;
    int a[1010][2];
    int tmp=0;
    int k=0;

    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&a[i][0],&a[i][1]);
    }
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            ans[k]=((a[i][0]-a[j][0])*(a[i][0]-a[j][0]))+((a[i][1]-a[j][1])*(a[i][1]-a[j][1]));
            k++;
        }
    }
    for(int i=0;i<k-1;i++){
        for(int j=0;j<k-i-1;j++){
            if(ans[j]>ans[j+1]){
                tmp=ans[j+1];
                ans[j+1]=ans[j];
                ans[j]=tmp;
            }
        }
    }
    for(int i=0;i<k;i++){
        printf("%d\n",ans[i]);
    }
    return 0;

}