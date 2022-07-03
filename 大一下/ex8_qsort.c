#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char name[1000];
    char attribute[10];
    int att;
    int attack;
    int hp;
} inf;


int name_cmp(const void* ta,const void* tb){
    inf* a = (inf*) ta;
    inf* b = (inf*) tb;
    return strcmp(a -> name,b -> name);
}

int attack_cmp(const void* ta,const void* tb){
    inf* a = (inf*) ta;
    inf* b = (inf*) tb;
    int c = a -> attack;
    int d = b -> attack;
    if(c < d){
        return 1;
    }
    else if(c == d){
        return 0;
    }
    else if(c > d){
        return -1;
    }
}

int hp_cmp(const void* ta,const void* tb){
    inf* a = (inf*) ta;
    inf* b = (inf*) tb;
    int c = a -> hp;
    int d = b -> hp;
    if(c > d){
        return 1;
    }
    else if(c == d){
        return 0;
    }
    else if(c < d){
        return -1;
    }
}

int attribute_cmp(const void* ta,const void* tb){
    inf* a = (inf*) ta;
    inf* b = (inf*) tb;
    int c = a -> att;
    int d = b -> att;
    if(c > d){
        return 1;
    }
    else if(c == d){
        return hp_cmp(a,b);
    }
    else if(c < d){
        return -1;
    }
}


void run(inf* pokemon,int n,int m,char ask[]){
    for(int i=0;i<n;i++){
        scanf("%s %s %d %d",pokemon[i].name,pokemon[i].attribute,&pokemon[i].attack,&pokemon[i].hp);
    }
    for(int i=0;i<m;i++){
        scanf("%s",ask);
        printf("Case #%d:\n",i+1);
        if(strcmp(ask,"NAME") == 0){
            qsort(pokemon,n,sizeof(inf),name_cmp);
        }
        else if(strcmp(ask,"ATTRIBUTE") == 0){
            char five_att[][10] = {"WATER","FIRE","EARTH","LIGHT","DARK"};
            for(int j=0;j<n;j++){
                int temp;
                for(int k=0;k<5;k++){
                    if(strcmp(pokemon[j].attribute,five_att[k]) == 0){
                        temp = k;
                    }
                }
                pokemon[j].att = temp;
            }
            qsort(pokemon,n,sizeof(inf),attribute_cmp);
        }
        else if(strcmp(ask,"ATTACK") == 0){
            qsort(pokemon,n,sizeof(inf),attack_cmp);
        }
        else if(strcmp(ask,"HP") == 0){
            qsort(pokemon,n,sizeof(inf),hp_cmp);
        }
        for(int j=0;j<n;j++){
            printf("%s %s %d %d\n",pokemon[j].name,pokemon[j].attribute,pokemon[j].attack,pokemon[j].hp);
        }
    }
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    inf pokemon[n];
    char ask[10];
    run(pokemon,n,m,ask);
}