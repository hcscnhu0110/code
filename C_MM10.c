#include <stdio.h>

int main(){
    double c;
    while(scanf("%lf", &c) != EOF){
        printf("%.1f\n", c * 9 / 5 + 32);
    }
}