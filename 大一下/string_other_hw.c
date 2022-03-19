#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void judge(char* input,char* old,char* new,char* parameter,int* flag){
    int cnt = 1;
    const char* d = " \n\t,./<>?:;[]{}/*+_()&^$";
    char* p;
    p = strtok(input,d);
    if(p == NULL){
        cnt = 1;
    }
    else{
        strcpy(old,p);
    }

    while(p != NULL){
        cnt++;
        p = strtok(NULL,d);
        if(cnt == 2){
            if(p == NULL){
                continue;
            }
            else{
                strcpy(new,p);
            }
        }
        else if(cnt == 3){
            *flag = 1;
            if(p == NULL){
                continue;
            }
            else{
                strcpy(parameter,p);
            }
        }
    }
    if((strcmp(parameter,"-i") != 0 && cnt == 4) || cnt > 4 || cnt < 3){
        printf("The input format: string1 string2 [parameter]");
        exit(0);
    }
}

void replace(char* article,char* old,char* new){
    int lens = strlen(article);
    for(int i=0;i<lens;i++){
        
    }
}

int main(){
    char input[210];
    fprintf(stderr,"Enter pattern, replacement, and at most one parameter:");
    fgets(input,210,stdin);
    char old[110],new[110],parameter[10];
    int flag = 0;
    judge(input,old,new,parameter,&flag);

    char input2[5000];
    char article[5000];
    memset(article,'\0',sizeof(article));
    while(fgets(input2,5000,stdin) != NULL){
        strcat(article,input2);
    }
    if(!flag){
        
    }
    
}