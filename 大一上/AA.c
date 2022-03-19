#include <stdio.h>

int main()
{
    int n[100000];
    int i,idx= 1;
    while(scanf("%d",&i) && i)
    {
        n[i]= idx;
        idx = idx +1;
    }
    // n[1]=5  n[2]=1  n[3]= 2  n[4]=4  n[5]=3
    for(int i= 1;i< idx;i++)
        printf("%d ",n[i]);
    printf("\n");
}