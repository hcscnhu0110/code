#include <stdio.h>
#include <string.h>

struct data{
    char name[101];
    unsigned long long int id;
    int score[3];
};


int main(){
    int n,q;
    int num;
    char name2[101];
    char sub;
    unsigned long long int id2;
    struct data student[1010];

    scanf("%d %d",&n,&q);
    for(int i=0;i<n;i++){
        scanf("%s %llu %d %d %d",student[i].name,&student[i].id,&student[i].score[0],&student[i].score[1],&student[i].score[2]);
    }
    for(int i=0;i<q;i++){
        scanf("%d",&num);
        if(num == 1){
            scanf("%s",name2);
            for(int j=0;j<n;j++){
                if(strcmp(student[j].name,name2) == 0){
                    printf("%llu\n",student[j].id);
                }
            }
        }
        else if(num == 2){
            scanf("%s %c",name2,&sub);
            for(int j=0;j<n;j++){
                if(strcmp(student[j].name,name2) == 0 && sub == 'L'){
                    printf("%d\n",student[j].score[0]);
                }
                else if(strcmp(student[j].name,name2) == 0 && sub == 'C'){
                    printf("%d\n",student[j].score[1]);
                }
                else if(strcmp(student[j].name,name2) == 0 && sub == 'E'){
                    printf("%d\n",student[j].score[2]);
                } 
            }
        }           
        else if(num == 3){
            scanf("%llu",&id2);
            for(int j=0;j<n;j++){
                if(student[j].id == id2){
                    printf("%s\n",student[j].name);
                }
            }
        }
        else if(num == 4){
            scanf("%llu %c",&id2,&sub);
            for(int j=0;j<n;j++){
                if(student[j].id == id2 && sub == 'L'){
                    printf("%d\n",student[j].score[0]);
                }
                else if(student[j].id == id2 && sub == 'C'){
                    printf("%d\n",student[j].score[1]);
                }
                else if(student[j].id == id2 && sub == 'E'){
                    printf("%d\n",student[j].score[2]);
                }
            }
        }
    }
    return 0;    
}