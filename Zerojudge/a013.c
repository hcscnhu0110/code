#include <stdio.h>
#include <string.h>

int plus(char n[][1000],int lens,int k){
    int count=0;
    for(int i=0;i<lens;i++){
        if(n[k][i]=='I'){
            if(n[k][i+1]=='X'){
                count+=9;
                i++;
            }
            else if(n[k][i+1]=='V'){
                count+=4;
                i++;
            }
            else{
                count+=1;
            }
            
        }
        else if(n[k][i]=='V'){
            count+=5;
        }
        else if(n[k][i]=='X'){
            if(n[k][i+1]=='L'){
                count+=40;
                i++;
            }
            else if(n[k][i+1]=='C'){
                count+=90;
                i++;
            }
            else{
                count+=10;
            }
        }
        else if(n[k][i]=='L'){
            count+=50;
        }
        else if(n[k][i]=='C'){
            if(n[k][i+1]=='D'){
                count+=400;
                i++;
            }
            else if(n[k][i+1]=='M'){
                count+=900;
                i++;
            }
            else{
                count+=100;
            }
        }
        else if(n[k][i]=='D'){
            count+=500;
        }
        else if(n[k][i]=='M'){
            count+=1000;
        }
    }
    return count;
}

char trans(int ans[],int i){
    if(ans[i]==1000){
        return 'M';
    }
    else if(ans[i]==500){
        return 'D';
    }
    else if(ans[i]==100){
        return 'C';
    }
    else if(ans[i]==50){
        return 'L';
    }
    else if(ans[i]==10){
        return 'X';
    }
    else if(ans[i]==5){
        return 'V';
    }
    else if(ans[i]==1){
        return 'I';
    }
}


int main(){
    int R[10]={1000,500,100,50,10,5,1,0};
    char n[2][1000];
    int temp1,temp2;
    int a;
    int ans[1000];
    int count=0;
    char result[1000];

    while(scanf("%s",n[0]) && n[0][0]!= '#'){
        scanf("%s",n[1]);
        int t=0;
        int k=0;
        int lens1=strlen(n[0]);
        int lens2=strlen(n[1]);
        temp1=plus(n,lens1,k);
        k+=1;
        temp2=plus(n,lens2,k);
        a= (temp1 >= temp2) ? temp1-temp2 : temp2-temp1;

        if(a==0){
            printf("ZERO");
        }

        while(a != 0){
            for(int i=0;i<7;i++){
                if(a < 1000 && a >= 900){
                    a=a-900;
                    ans[t]=100;
                    ans[t+1]=1000;
                    i=2;
                    t+=2;
                    count+=2;
                }
                else if(a < 500 && a >=400){
                    a=a-400;
                    ans[t]=100;
                    ans[t+1]=500;
                    i=2;
                    t+=2;
                    count+=2;
                }
                else if(a < 100 && a >= 90){
                    a=a-90;
                    ans[t]=10;
                    ans[t+1]=100;
                    i=4;
                    t+=2;
                    count+=2;
                }
                else if(a < 50 && a >= 40){
                    a=a-40;
                    ans[t]=10;
                    ans[t+1]=50;
                    i=4;
                    t+=2;
                    count+=2;
                }
                else if(a == 9){
                    a=a-9;
                    ans[t]=1;
                    ans[t+1]=10;
                    t+=2;
                    count+=2;
                }
                else if(a == 4){
                    a=a-4;
                    ans[t]=1;
                    ans[t+1]=5;
                    t+=2;
                    count+=2;
                }
                else{
                    if(a/R[i] >= 1){
                        ans[t]=R[i];
                        a=a-R[i];
                        if(a > R[i+1]){
                            ans[t+1]=R[i+1];
                            i--;
                        }
                        t++;
                        count++;
                    }
                }
            }
        }

        for(int i=0;i<count;i++){
            result[i]=trans(ans,i);
            printf("%c",result[i]);
        }
        count=0;
        printf("\n");
    }
    return 0;
}