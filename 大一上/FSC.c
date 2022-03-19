#include <stdio.h>
#include <string.h>
int main(){
    int n;
    scanf("%d",&n);
    char arr[2*n-1];
    memset(arr,' ',sizeof(arr));
    int mid = n-1;
    for(int i =0;i<n;i++){
        arr[mid +i]='*';
        arr[mid-i] ='*';
        for(int j =0;j<2*n-1;j++){
            printf("%c",arr[j]);
        }
        arr[mid +i]=' ';
        arr[mid-i] =' ';
        printf("\n");
    }
    for(int i = n-2;i>=0;i--){
        arr[mid +i]='*';
        arr[mid-i] ='*';
        for(int j =0;j<2*n-1;j++){
            printf("%c",arr[j]);
        }
        arr[mid +i]=' ';
        arr[mid-i] =' ';
        printf("\n");
    }
}