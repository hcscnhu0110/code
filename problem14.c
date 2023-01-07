#include <stdio.h>
#include <string.h>

int main(){
    char input[1000];
    while(scanf("%s", input) != EOF){
        int start = 0;
        int end = strlen(input) - 1;
        int flag = 1;
        while(start < end){
            if(input[start] != input[end]){
                flag = 0;
                break;
            }
            start++;
            end--;
        }
        if(flag){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
}