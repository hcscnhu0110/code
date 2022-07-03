#include <stdio.h>
#include <string.h>

int main(){
    char a[10000];
    gets(a);
    int lens=strlen(a);
    for(int i=0;i<lens;i++){
        a[i]=a[i]-7;
        if(a[i]>12)
        printf("%c",a[i]);
    }
    return 0;
}