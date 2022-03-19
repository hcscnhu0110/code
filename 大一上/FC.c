#include <stdio.h>

int judge1(char a[][4]){
    int c1=0,c2=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(a[i][j]=='O'){
                c1++;
            }
            else if(a[i][j]=='X'){
                c2++;
            }
        }
    }
    if(c1-c2>1 || c2-c1>1){
        return 0;
    }
    else{
        return 1;
    }
}

int judge2(char a[][4]){
    if(a[0][0]==a[0][1] && a[0][1]==a[0][2] && a[1][0]==a[1][1] && a[1][1]==a[1][2]){
        return 0;
    }
    else if(a[0][0]==a[0][1] && a[0][1]==a[0][2] && a[2][0]==a[2][1] && a[2][1]==a[2][2]){
        return 0;
    }
    else if(a[1][0]==a[1][1] && a[1][1]==a[1][2] && a[2][0]==a[2][1] && a[2][1]==a[2][2]){
        return 0;
    }
    else if(a[0][0]==a[1][0] && a[1][0]==a[2][0] && a[0][1]==a[1][1] && a[1][1]==a[2][1]){
        return 0;
    }
    else if(a[0][0]==a[1][0] && a[1][0]==a[2][0] && a[0][2]==a[1][2] && a[1][2]==a[2][2]){
        return 0;
    }
    else if(a[0][1]==a[1][1] && a[1][1]==a[2][1] && a[0][2]==a[1][2] && a[1][2]==a[2][2]){
        return 0;
    }
    else{
        return 1;
    }
}

int lh(char a[][4]){
    if(a[0][0]=='O' && a[0][0]==a[0][1] && a[0][1]==a[0][2]){
        return 0;
    }
    else if(a[0][0]=='O' && a[0][0]==a[1][0] && a[1][0]==a[2][0]){
        return 0;
    }
    else if(a[0][0]=='O' && a[0][0]==a[1][1] && a[1][1]==a[2][2]){
        return 0;
    }
    else if(a[2][2]=='O' && a[2][2]==a[2][1] && a[2][1]==a[2][0]){
        return 0;
    }
    else if(a[2][2]=='O' && a[2][2]==a[1][2] && a[1][2]==a[0][2]){
        return 0;
    }
    else if(a[0][2]=='O' && a[0][2]==a[1][1] && a[1][1]==a[2][0]){
        return 0;
    }
}

int yf(char a[][4]){
    if(a[0][0]=='X' && a[0][0]==a[0][1] && a[0][1]==a[0][2]){
        return 0;
    }
    else if(a[0][0]=='X' && a[0][0]==a[1][0] && a[1][0]==a[2][0]){
        return 0;
    }
    else if(a[0][0]=='X' && a[0][0]==a[1][1] && a[1][1]==a[2][2]){
        return 0;
    }
    else if(a[2][2]=='X' && a[2][2]==a[2][1] && a[2][1]==a[2][0]){
        return 0;
    }
    else if(a[2][2]=='X' && a[2][2]==a[1][2] && a[1][2]==a[0][2]){
        return 0;
    }
    else if(a[0][2]=='X' && a[0][2]==a[1][1] && a[1][1]==a[2][0]){
        return 0;
    }
}

int main(){
    char a[4][4];
    int j;
    for(int i=0;i<3;i++){
        scanf("%s",a[i]);
    }
    if(judge1(a)==0){
        printf("Cheat");
    }
    else if(judge1(a)==1){
        if(judge2(a)==0){
            printf("Cheat");
        }
        else if(judge2(a)==1){
            if(lh(a)==0){
                printf("LH win");
            }
            else if(yf(a)==0){
                printf("YF win");
            }
            else{
                printf("Tie");
            }
        }
    }
    return 0;
}