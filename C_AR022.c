#include <stdio.h>
#include <string.h>

int main(){
    int alpha[30] = {0};
    char word[1000];
    while(gets(word) != NULL){
        int len = strlen(word);
        for(int i = 0; i < len; i++){
            if(word[i] >= 'a' && word[i] <= 'z'){
                alpha[word[i] - 'a'] += 1;
            }
            else if(word[i] >= 'A' && word[i] <= 'Z'){
                alpha[word[i] - 'A'] += 1;
            }
        }
        printf("%d", alpha[0]);
        for(int i = 1; i < 26; i++){
            printf(" %d", alpha[i]);
        }
        printf("\n");
    }
}