#include <stdio.h>

int main()
{
    float x,y;
    int k;
    scanf("%f %f %d",&x,&y,&k);
    printf("%.*f\n",k,x+y);
    return 0;
}