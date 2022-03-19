#include <stdio.h>
#include <math.h>

double distance(double x1,double y1,double x2,double y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}

int main(){
    double a,b,c,d;
    while(scanf("%lf%lf%lf%lf",&a,&b,&c,&d) != EOF){
        double result=distance(a,b,c,d);
        printf("%f\n",result);
    }
    return 0;
}