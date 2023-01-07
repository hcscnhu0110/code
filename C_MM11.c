#include <stdio.h>

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        int money[3] = {10, 5, 1};
        for(int i = 0; i < 3; i++){
            printf("NT%d=%d\n", money[i], n / money[i]);
            n %= money[i];
        }
    }
}