#include <stdio.h>

double sum(double x,double y,double z){
    return x+y+z;
}

int main(){
    double a,b,c,d;
    scanf("%lf %lf %lf %lf",&a,&b,&c,&d);
    double result=sum(a,b,c);
    if(result > (d+0.000001)){
        printf("Greater than");
    }
    else if(result <= (d+0.000001) && result >= (d-0.000001)){
        printf("Equal to");
    }
    else if(result < (d-0.000001)){
        printf("Less than");
    }
    return 0;
}