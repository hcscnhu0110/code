#include <stdio.h>

int main(){
    char phone[4][10]={0},tmp=0,n;
    printf("input phone number: ");
    for(n=0; n<4 && tmp != '\n'; n++){
        scanf("%*[-() ]");
        scanf("%[0-9]",phone[n]);
        tmp=getchar();
    }
    for(int i=0;i<n;i++){
        puts(phone[i]);
    }
}