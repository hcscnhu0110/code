#include <stdio.h>

void factorial(int* bomb,int key){
    if(bomb[key] == 1){
        bomb[key]=0;
   }
    else if(bomb[key] == 2){
        bomb[key]=0;
        factorial(bomb,key-1);
        factorial(bomb,key+1);
        
    }
    else if(bomb[key] >= 3){
        int x=bomb[key];
        bomb[key]=0;
        factorial(bomb,key-x);
        factorial(bomb,key-x*2);
        factorial(bomb,key+x);
        factorial(bomb,key+x*2);
        
    }
}

int main(){
    int N;
    int bomb[2000]={0};
    int key;

    scanf("%d",&N);
    for(int i=20;i<N+20;i++){
        scanf("%d",&bomb[i]);
    }
    scanf("%d",&key);
    factorial(bomb,key+20);
    for(int i=20;i<N+20;i++){
        printf("%d ",bomb[i]);
    }
    printf("\n");
    return 0;
}