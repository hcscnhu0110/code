#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int cnt=0, len, w=0;
    char k[1001], invk[1001];
    unsigned int t[126];
    
    scanf("%s", k);
    while(scanf("%d", &t[cnt++])!=EOF);
    len=strlen(k);
    cnt-=1;

    while(len!=cnt*4){
        if (len>cnt*4){
            k[len-1]='\0';
            len--;
        }
        else{
            k[len]=k[w++];
            len++;
            k[len]='\0';
        }
    }

    for (int i=len-1; i>=0; i--){
        invk[len-1-i]=k[i];
    }
    invk[len]='\0';
    
    for (int i=0; i<cnt; i++){
        unsigned int a=0x80000000;
        for (int l=0; l<4; l++){
            unsigned int tmp=0;
            for (int j=0; j<8; j++){
                tmp<<=1;
                if (a&t[i]) tmp=tmp|1;
                a>>=1;
            }
            printf("%c", tmp^k[(4*i+l)%len]^invk[(4*i+l)%len]);
        }
    }

    return 0;
}