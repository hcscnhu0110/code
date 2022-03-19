#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    int count1=0,count2=0,count3=0;

    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        if(a[i] == 1){
            count1++;
        }
        else if(a[i] == 2){
            count2++;
        }
        else if(a[i] == 3){
            count3++;
        }
    }
    for(int i=0;i<n;i++){
        if(i < count1){
            a[i] = 1;
        }
        else if(i >= count1 && i < count1+count2){
            a[i] = 2;
        }
        else if(i >= count1+count2 && i < count1+count2+count3){
            a[i] = 3;
        }
        printf("%d ",a[i]);
    }
    return 0;
}