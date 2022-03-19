#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int a=n+1,b=n+2,c=n+3,d=n+4;
    printf("0 %d %d %d %d %d %d %d %d %d",n,a,-a,b,-b,c,-c,d,-d); 
    return 0;
}

/*
int main(){
    int n;
    scanf("%d", &n);
    printf("-101 -102 -103 -104 -105 101 102 103 209 %d\n", n);
    return 0;
}
*/