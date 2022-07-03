#include <stdio.h>

int main(){
    int t;
    scanf("%d ", &t);
    for(int i = 0; i < t; i++){
        char input;
        int value;
        int sum = 1;
        while((input = getchar()) != '\n'){
            value = 0 + input - '0';
            sum = sum * value;
        }
        printf("%d\n", sum);
    }
}