#include <stdio.h>

int main(){
    int n;
    int k=0,l=0,m=1;
    int ans0[10000];
    int ans1[10000];
    int ans2[100]={0};
    int count1=1,count2=0,count3=0;
    int lens;
    

    scanf("%d",&n);
    int N=n;
    while(n != 1){
        for(int i=2;i<=N;i++){
            if(n%i==0){
                n=n/i;
                ans0[k]=i;
                i=i-1;
                if(k>=1){
                    if(ans0[k]==ans0[k-1]){
                        count1++;
                        ans2[l]=count1;
                        count3++;
                    }
                    else{
                        ans1[m]=ans0[k];
                        l++;
                        count1=1;
                        m++;
                    }
                }
                k++;
                count2++;
            }
            else{
                continue;
            }
        }
        ans1[0]=ans0[0];
    }
    lens=count2-count3;
    for(int i=0;i<lens;i++){
        if(ans2[i]==0){
            printf("%d",ans1[i]);
            if(i != lens-1){
                printf(" * ");
            }
        }
        else{
            printf("%d",ans1[i]);
            printf("^");
            printf("%d",ans2[i]);
            if(i != lens-1){
                printf(" * ");
            }
        }
    }
    return 0;    
}