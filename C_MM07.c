#include <stdio.h>

int main(){
    int x;
    while(scanf("%d", &x) != EOF){
        printf("%d %d %d\n", x, x * x, x * x * x);
    }
}