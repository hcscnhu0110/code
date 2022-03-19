#include <stdio.h>

int main(){
    char c[12];
    int i;
    scanf("%s",c);
    for(i=0;i<=9;i++){
        if(c[i]>='A' && c[i]<='Z'){
            c[i]+=c[10]-'0';
            if(c[i]>'Z'){
            c[i]-=26;
            }
        }
        else{
            c[i]+=c[10]-'0';
            if(c[i]>'z'|| c[i]<0){
            c[i]-=26;
            }
        }
    }
    printf("%c%c%c%c%c%c%c%c%c%c",c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9]);
    return 0;
}