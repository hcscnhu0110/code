#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int count1 = 0, count2 = 0, count3 = 0;
    for(int i = 0; i < n; i++){
        int input;
        scanf("%d", &input);
        if(input % 3 == 0){
            count1++;
        }
        else if(input % 3 == 1){
            count2++;
        }
        else if(input %3 == 2){
            count3++;
        }
    }
    printf("%d %d %d", count1, count2, count3);
}