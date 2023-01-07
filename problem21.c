#include <stdio.h>

int main(){
    double input[15];
    double max = 0;
    double min = 1000000;
    for(int i = 0; i < 10; i++){
        scanf("%lf", &input[i]);
        if(input[i] > max){
            max = input[i];
        }
        if(input[i] < min){
            min = input[i];
        }
    }
    printf("maximum:%.2f\n", max);
    printf("minimum:%.2f\n", min);
}