#include <stdio.h>

int main(){
    double x, y, h;
    while(scanf("%lf %lf %lf", &x, &y, &h) != EOF){
        printf("Trapezoid area:%.1f\n", (x + y) * h / 2);
    }
}