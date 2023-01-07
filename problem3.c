#include <stdio.h>

int main(){
    int x, y;
    while(scanf("%d %d", &x, &y) != EOF){
        if(x * x + y * y > 10000){
            printf("outside\n");
        }
        else{
            printf("inside\n");
        }
    }
}