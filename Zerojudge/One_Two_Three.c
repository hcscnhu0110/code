#include <stdio.h>
#include <string.h>

int main(){
    int n;
    scanf("%d",&n);
    char voc[10][n];
    for(int i=0;i<n;i++){
        int count1 = 0, count2 = 0, count3 = 0;
        scanf("%s",voc[i]);
        int lens = strlen(voc[i]);
        for(int j=0;j<lens;j++){
            if(voc[i][j] == 'o' && j == 0 || voc[i][j] == 'n' && j == 1 || voc[i][j] == 'e' && j == 2){
                count1++;
            }
            else if(lens == 3 && voc[i][j] == 't' && j == 0 || voc[i][j] == 'w' && j == 1 || voc[i][j] == 'o' && j == 2){
                count2++;
            }
            else if(voc[i][j] == 't' && j == 0 || voc[i][j] == 'h' && j == 1 || voc[i][j] == 'r' && j == 2 || voc[i][j] == 'e' && j == 3 || voc[i][j] == 'e' && j == 4){
                count3++;
            }
        }
        if(count1 >= 2){
            printf("1\n");
        }
        else if(count2 >= 2){
            printf("2\n");
        }
        else if(count3 >= 4){
            printf("3\n");
        }
    }
}