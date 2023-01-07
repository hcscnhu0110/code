#include <stdio.h>
#include <math.h>

int main(){
    double input;
    while(scanf("%lf", &input) != EOF){
        printf("%.1f\n", floor(input * input * 10 + 0.5) / 10);
    }
}