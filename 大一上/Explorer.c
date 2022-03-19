#include <stdio.h>
#include <string.h>

int main(){
    int x=0,y=0;
    char a[1000000000];
    scanf("%s",a);
    int lens=strlen(a);
    for(int i=0;i<lens;i++){
        if(a[i]=='U'){
            y++;
        }
        else if(a[i]=='D'){
            y--;
        }
        else if(a[i]=='L'){
            x--;
        }
        else if(a[i]=='R'){
            x++;
        }
        else if(a[i]=='X'){
            break;
        }
    }
    printf("%d %d",x,y);
    return 0;
}
