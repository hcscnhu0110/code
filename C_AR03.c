#include <stdio.h>

int main(){
    int input;
    int sum = 0;
    for(int i = 0; i < 6; i++){
        scanf("%d", &input);
        sum += input * input * input;
    }
    printf("%d\n", sum);
}