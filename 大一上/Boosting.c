#include <stdio.h>
#include <string.h>

int main(){
    char name[510][110];
    int n=0;
    char tmp[110];
    while(scanf("%s",name[n]) != EOF){
        n++;
    }
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(strcmp(name[j],name[j+1]) > 0){
                strcpy(tmp,name[j+1]);
                strcpy(name[j+1],name[j]);
                strcpy(name[j],tmp);
            }
        }
    }

    for(int i=0;i<n;i++){
        printf("%s\n",name[i]);
    }
return 0;    
}