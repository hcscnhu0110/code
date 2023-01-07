#include <stdio.h>

int main(){
    int a[110];
    int i = 0;
    while(scanf("%d", &a[i]) != EOF){
        i++;
    }
    printf("%d", a[i - 1]);
    for(int j = i - 2; j >= 0; j--){
        printf(" %d", a[j]);
    }
    printf("\n");
}