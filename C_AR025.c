#include <stdio.h>
#include <string.h>

int main(){
    char input[1000];
    while(scanf("%s", input) != EOF){
        int ascii[1000] = {0};
        int len = strlen(input);
        for(int i = 0; i < len; i++){
            ascii[input[i] - 32] += 1;
        }
        for(int i = 96; i >= 0; i--){
            if(ascii[i]){
                printf("%d %d\n", i + 32, ascii[i]);
            }
        }
    }
}