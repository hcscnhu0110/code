#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char str[100010], key[100010], ans[100010];
    scanf("%s%s",str,key);
    int lens1=strlen(str),lens2=strlen(key);
    for(int i=0;i<=lens1;i++){
        key[i]=toupper(key[i]);
        if(str[i] >= 'A' && str[i] <= 'Z'){
            ans[i]=str[i]+(key[i%lens2]-65);
            if(ans[i] > 'Z'){
                ans[i]-=26;
            }
        }
        else if(str[i] >= 'a'){
            ans[i]=str[i]+(key[i%lens2]-65);
            if(ans[i] > 'z' || ans[i] < 0){
            ans[i]-=26;
            }
        }     
    }
    ans[lens1]='\0';
    printf("%s",ans);
    return 0;
}