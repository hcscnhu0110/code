#include <stdio.h>

void swap(char* a, char* b){
    char tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(){
    char a, b;
    scanf("%c %c", &a, &b);
    if(a > b){
        swap(&a, &b);
    }
    printf("%c %c", a, b);
}