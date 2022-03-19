#include <stdio.h>

int main(){
    int M,D,S;
    scanf("%d %d",&M,&D);
    S=(M*2+D)%3;
    if(S==0){
        printf("´¶³q");
    }
    else if(S==1){
        printf("¦N");
    }
    else if(S==2){
        printf("¤j¦N");
    }
    return 0;
}