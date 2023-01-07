#include <stdio.h>

int main(){
    int height, sex;
    while(scanf("%d %d", &height, &sex) != EOF){
        double weight;
        if(sex == 1){
            weight = (height - 80) * 0.7;
        }
        else{
            weight = (height - 70) * 0.6;
        }
        printf("%.1f\n", weight);
    }
}