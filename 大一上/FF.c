#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    int t;
    char n[110][40];
    char m[110][40];
    int p[110][1];
    char ask[0][40];
    int k=1;
    int lens;

    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%s",n[i]);
        scanf("%s",m[i]);
        scanf("%d",&p[i][0]);
    }
    while(scanf("%s",ask[0])!=EOF){
        lens=strlen(ask[0]);
        printf("case %d:\n",k);
        for(int i=0;i<t;i++){
            if(strncmp(n[i],ask[0],lens)==0){
                printf("%s\n",n[i]);
                printf("%s\n",m[i]);
                printf("%d\n",p[0][0]);
            }
        }
        k++;

    }
    //printf("%d",p[0][0]);
    
}