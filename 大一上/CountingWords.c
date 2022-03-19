#include <stdio.h>

int word(char c){
    if((c >= 'A' && c<= 'Z') || (c >= 'a' && c <= 'z')){
        return 1;
    }
    return 0;
}

int main(){
    char c;
    int judge=0,count=0;
    while((c=getchar()) != EOF){
        if(word(c)){
            if(judge==0){
                count+=1;
                judge=1;
            }
        }
        else{
            judge=0;
        }
    }
    printf("%d",count);
    return 0;
}