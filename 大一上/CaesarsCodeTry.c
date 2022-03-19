#include <stdio.h>

int main(){
    char a,b,c;
    int m[100]={0},n[100]={0},o[100]={0};
    int l[100];
    int one=1;
    int ten=0; 

    scanf("%c %c %c",&a,&b,&c);
    int x=(int)a,y=(int)b,z=(int)c;
    for(int i=7;i>=0;i--){
        m[i]=x%2;
        n[i]=y%2;
        o[i]=z%2;
        x=x/2;
        y=y/2;
        z=z/2;
    }
    for(int i=0;i<=7;i++){
        l[i]=(m[i]^n[i]^o[i]);
    }
    for(int i=7;i>=0;i--){
        ten+=l[i]*one;
        one=one*2;
    }
    printf("%X",ten);
}