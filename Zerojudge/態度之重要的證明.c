#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(){
    char voc[210];
    while(1){
        int count = 0;
        gets(voc);
        int lens = strlen(voc);
        if(voc[0] == '0' && lens == 1){
            break;
        }
        for(int i=0;i<lens;i++){
            if(isalpha(voc[i]) == 0){
                count = -1;
                break;
            }
            else{
                voc[i] = tolower(voc[i]);
                count += voc[i]-96;
            }
        }
        if(count == -1){
            printf("Fail\n");
        }
        else{
            printf("%d\n",count);
        }
    }
}