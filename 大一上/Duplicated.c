#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char word[1010][110];
    int n=0;
    char tmp[110];

    while(scanf("%s",word[n]) != EOF){
        n++;
    }
    
    for(int i=0;i < n;i++){
        strcpy(word[i],tolower(word[i]));
    }

    for(int i=0;i < n-1;i++){
        for(int j=0;j < n-i-1;j++){
            if(strcmp(word[j],word[j+1]) > 0){
                strcpy(tmp,word[j+1]);
                strcpy(word[j+1],word[j]);
                strcpy(word[j],tmp);
            }
        }
    }
}