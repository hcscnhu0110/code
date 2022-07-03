#include <stdio.h>

int main(){
    char input[10];
    int ans[10];
    for(int i = 0; i < 7; i++){
        scanf("%c", &input[i]);
        if(i > 0){
            if(input[i] >= input[i - 1]){
                char ans = input[i] - input[i - 1] + '0';
                printf("%c", ans);
            }
            else if(input[i] < input[i - 1]){
                char ans = input[i - 1] - input[i] + '0';
                printf("%c", ans);
            }
        }
    }
}