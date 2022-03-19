#include <stdio.h>

void test(int a[],int i){
    a[i]++;
}

int main(){
    int a[100];
    for(int i=0;i<5;i++){
        scanf("%d",&a[i]);
        test(a,i);
        printf("%d ",a[i]);
    }

}