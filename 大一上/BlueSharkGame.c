#include <stdio.h>

int compare(int count1,int count2){
    if(count1 >= count2){
        return count1;
    }
    else{
        return count2;
    }
}

int main(){
    long long int x0,y0;
    int count1=0,count2=0;
    long long int a[100]={0},b[100]={0};
    scanf("%lld %lld",&x0,&y0);
    long long int x=x0,y=y0;
    while(x0 >= 2){
        x0=x0/2;
        count1++;
    }
    while(y0 >= 2){
        y0=y0/2;
        count2++;
    }
    int result=compare(count1,count2);

    for(int i=result;i>=0;i--){
        a[i]=x%2;
        b[i]=y%2;
        x=x/2;
        y=y/2;
    }

    long long int ans1=0,ans2=0,ans3=0;
    for(int i=0;i<=result;i++){
        if(a[i]&b[i] == 1){
            ans1++;
        }
        if(a[i]|b[i] == 1){
            ans2++;
        }
        if(a[i]^b[i] == 1){
            ans3++;
        }
    }
    printf("%lld %lld %lld",ans1,ans2,ans3);
    return 0;
}