#include <stdio.h>

int main(){
    int q[10];
    int n;
    int ask[10];
    int countA=0,countB=0;
    int temp=0;

    for(int i=0;i<4;i++){
        scanf("%d",&q[i]);
    }

    scanf("%d",&n);

    for(int i=0;i<n;i++){
        for(int j=0;j<4;j++){
            scanf("%d",&ask[j]);
        }
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(ask[j] == q[k] && j == k){
                    countA++;
                    break;
                }
                else if(ask[j] == q[k] && j != k){
                    int find=k;
                    if(q[find] == ask[find]){
                        continue;
                    }
                    else{
                        countB++;
                        break;
                    }
                }
            }
        }
        printf("%dA%dB\n",countA,countB);
        countA=0;
        countB=0;
    }
    return 0;
}