#include <stdio.h>
#include <string.h>

int main(){
    int input;
    scanf("%d", &input);
    int bin[10] = {0};
    if(input < 0){
        input += 256;
    }
    int count = 0;
    while(input >= 2){
        bin[count++] = input % 2;
        input /= 2;
    }
    bin[count] = input;
    for(int i = 7; i >= 0; i--){
        printf("%d", bin[i]);
    }
    printf("\n");
}