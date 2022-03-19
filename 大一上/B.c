#include <stdio.h>

int main()
{
    int x;
    scanf ("%d",&x);
    while (x < 60)
    {
        x==0;
        printf("%d",x);
    }
    while (60<=x<=80)
    {
        x+=220-x*2;
        printf("%d",x);
    }
    while (x > 80)
    {
        x+=x-20;
        printf("%d",x);
    }
}
