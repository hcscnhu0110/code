#include <stdio.h>
#include <string.h>

int main(){
    char input[110];
    while(gets(input) != NULL){
        int ans[30] = {0};
        int count = 0;
        const char *delim = " ,.";
        char *voc;
        voc = strtok(input, delim);

        while(voc != NULL){
            count++;
            int len = strlen(voc);
            for(int i = 0; i < len; i++){
                if(voc[i] >= 'a'){
                    ans[voc[i] - 'a'] += 1;
                }
                else{
                    ans[voc[i] - 'A'] += 1;
                }
            }
            voc = strtok(NULL, delim);
        }
        
        printf("%d\n", count);
        for(int i = 0; i < 26; i++){
            if(ans[i]){
                printf("%c : %d\n", i + 97, ans[i]);
            }
        }
    }
}