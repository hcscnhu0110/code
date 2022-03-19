#include <stdio.h>

int search(int a[],int n){
    int temp = a[0];
    int k;
    for(int i=1;i<n;i++){
        if(a[i] < temp){
            temp = a[i];
            k=i;
        }
    }
    return k;
}

int a1[300010],a2[300010];

void judge(int a[],int n){
    int site = search(a,n);
    long long int sum1=0,sum2=0;
    int count1=0,count2=0;
    int j=0,k=0;

    for(int i=0;i<=site-1;i++){
        sum1+=a[i];
        count1++;
        a1[j]=a[i];
        j++;
    }
    for(int i=site+1;i<n;i++){
        sum2+=a[i];
        count2++;
        a2[k]=a[i];
        k++;
    }
    if(sum1 > sum2){
        n=count1;
        if(n != 1){
            judge(a1,n);
        }
        else{
            printf("%d",a1[0]);
        }
    }
    else if(sum1 < sum2 || sum1 == sum2){
        n=count2;
        if(n != 1){
            judge(a2,n);
        }
        else{
            printf("%d",a2[0]);
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    judge(a,n);
    return 0;
}