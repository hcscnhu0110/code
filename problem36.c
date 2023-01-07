#include <stdio.h>

int main(){
    int year;
    while(scanf("%d", &year) != EOF){
        if(!(year % 4)){
            if(year % 100){
                printf("Bissextile Year\n");
            }
            else{
                if(year % 400){
                    printf("Common Year\n");
                }
                else{
                    printf("Bissextile Year\n");
                }
            }
        }
        else{
            printf("Common Year\n");
        }
    }
}