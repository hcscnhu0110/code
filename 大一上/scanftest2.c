#include <stdio.h>
#include <string.h>

int main(){
    char number[100][10],n=0;
    memset(number,0,sizeof(number));
    do{
        scanf("%*[^0-9\n]");
        scanf("%[0-9]",number[n++]);
    }while(getchar() != '\n');
    puts("----------");
    for(int i=0;i<n;i++){
        puts(number[i]);
    }
}