#include <stdio.h>

int main(){
    int input;
    while(scanf("%d", &input) != EOF){
        int flag = 0;
        for(int i = 2; i * i <= input; i++){
            if(!(input % i)){
                flag = 1;
            }
        }
        if(flag){
            printf("NO\n");
        }
        else{
            printf("YES\n");
        }
    }
}