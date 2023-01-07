#include <stdio.h>
#include <string.h>

int main(){
    char input[1000];
    gets(input);
    int n;
    scanf("%d", &n);
    int len = strlen(input);
    for(int i = 0; i < len; i++){
        if(input[i] >= 'a' && input[i] <= 'z'){
            input[i] = (input[i] - 'a' + n) % 26 + 'a';
        }
        else if(input[i] >= 'A' && input[i] <= 'Z'){
            input[i] = (input[i] - 'A' + n) % 26 + 'A';
        }
        else if(input[i] >= '0' && input[i] <= '9'){
            input[i] = (input[i] - '0' + n) % 10 + '0';
        }
        printf("%c", input[i]);
    }
    printf("\n");
}