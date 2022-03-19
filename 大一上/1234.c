#include <stdio.h>
#include <stdlib.h>

int main(){
    int temp,pl=25,pr=10;
    int*a=&pl,*b=&pr;
    temp=*a;
    *a=*b;
    *b=temp;
    printf("%d %d",*a,*b);

    int *c=(int *) malloc(sizeof(int)*1);
    *c=25;
    int *d=(int *) malloc(sizeof(int)*1);
    *d=10;
    int tmp=*c;
    *c=*d;
    *d=tmp;

    int *arr=(int *) malloc(sizeof(int)*1000);
    arr[10]=100;
    printf("%d %d", arr[10], 10[arr]);
}
