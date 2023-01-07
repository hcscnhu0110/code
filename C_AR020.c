#include <stdio.h>

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        int input[1000];
        int flag = 1;
        for(int i = 0; i < n; i++){
            scanf("%d", &input[i]);
            for(int j = 0; j < i; j++){
                if(input[i] == input[j]){
                    flag = 0;
                    break;
                }
            }
        }
        if(flag){
            printf("1\n");
        }
        else{
            printf("0\n");
        }
    }
}