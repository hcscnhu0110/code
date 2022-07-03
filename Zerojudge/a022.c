#include <stdio.h>
#include <string.h>

int main(){
    char a[1010];
    gets(a);
    int lens=strlen(a);
    int mid=lens/2;
    int j=lens-1;
    int count=0;
    for(int i=0;i<mid;i++){
        if(a[i]==a[j]){
            count++;
            j--;
        }
        else{
            printf("no");
            break;
        }
    }
    if(count==mid){
        printf("yes");
    }   
    return 0;
}