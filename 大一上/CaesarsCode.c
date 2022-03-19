#include <stdio.h>


int main(){
    int x0;
    int count1=0;
    int a[100]={0};
    int ten[100]={0};
    int n=0;
    int binary[100]={0};

    scanf("%d",&x0);
    int x=x0;
    while(x0>=16){
        x0=x0/16;
        count1++;
    }
    for(int i=count1;i>=0;i--){
        a[i]=x%16;
        x=x/16;
    }
    for(int i=0;i<=count1;i+=2){
        ten[n]=a[i]*16+a[i+1]*1;
        n++;
    }
    for(int i=0;i<n;i++){
        
    }
}