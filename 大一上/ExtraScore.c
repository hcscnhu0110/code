#include <stdio.h>
#include <stdlib.h>

int mystrlen(char *s){
    int i=0;
    while(*s){
        s++;
        i++;
    }
    return i;
}

int main(){
    char s[40010];
    char *ss;

    while(fgets(s, 40010, stdin)!=NULL){
        int len=mystrlen(s);
        int score=0, tmp, flag=0;
        char tmp_s[10];
        if (s[len-1]=='\r'){
            s[len-1]='\0';
        } 
        ss=s;
        while(sscanf(ss, "%d", &tmp)!=EOF){
            score+=tmp;
            sscanf(ss, "%s", tmp_s);
            ss+=mystrlen(tmp_s);
            if (*ss==' ') {
                ss++;
                flag=1;
            }
        }
        if (flag==0){
            continue;
        }
        else{
            printf("%d\n", score);
        }
    }
    return 0;
}