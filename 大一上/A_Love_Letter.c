#include <stdio.h>

int main(){
    char c;
    int x,n;
    scanf("%d",&x);
    for(int a=0;a<x;a++){
        scanf(" %c %d",&c,&n);
        int d;
        d = c;
        d+=n%26;
        if(d>'z'){
            d-=26;
        }
        else if(d<'a'){
            d+=26;
        }
        c = d;
        printf("%c\n",c);
    }
    return 0;
}