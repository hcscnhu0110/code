#include <stdio.h>
#include <string.h>

int main(){
    char a[] = "abcdefg";
    char* p;
    char b[10];
    gets(b);
    p = strstr(a,b);
    printf("%s",p);
}