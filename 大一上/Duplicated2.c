#include <stdio.h>
#include <stdlib.h>

int myisupper(char c){
    if (c>='A' && c<='Z') return 1;
    return 0;
}

void mytolower(char *s){
    while(*s){
        if (myisupper(*s)) *s=*s-'A'+'a';
        s++;
    }
}

int mystrlen(char *s){
    int len=0;
    while(*s){
        s++;
        len++;
    }
    return len;
}

int mystrcmp(char *s1, char *s2){
    int i=0;
    while(1){
        if (s1[i]==s2[i]){
            if (s1[i]=='\0') return 0;
            i++;
        }
        else return s1[i]-s2[i];
    }
}

void mystrcpy(char *des, char *src){
    while(*src){
        *des++=*src++;
    }
    *des='\0';
}

int main(){
    int i=0;
    char s[101];
    char dic[1000][101];
    int cnt[1000]={0};

    while(scanf("%s", s)!=EOF){
        int len=mystrlen(s);
        int flag=0;
        if (s[len-1]=='\n') s[len-1]='\0';
        mytolower(s);
        
        for (int j=0; j<i; j++){
            if (mystrcmp(s, dic[j])==0){
                cnt[j]++;
                flag=1;
                break;
            }
        }
        if (flag==0){
            mystrcpy(dic[i], s);
            cnt[i]=1;
            i++;
        }
    }

    for (int j=0; j<i; j++){
        for (int k=0; k<i-j-1; k++){
            if (mystrcmp(dic[k], dic[k+1])>0){
                int tmp=cnt[k];
                cnt[k]=cnt[k+1];
                cnt[k+1]=tmp;
                mystrcpy(s, dic[k]);
                mystrcpy(dic[k], dic[k+1]);
                mystrcpy(dic[k+1], s);
            }
        }
    }

    for (int j=0; j<i; j++) printf("%s %d\n", dic[j], cnt[j]);

    return 0;
}