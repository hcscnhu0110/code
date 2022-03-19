#include <stdio.h>
#include <string.h>

int plus(char n[][1000],int lens,int k){
    int count=0;
    for(int i=0;i<lens;i++){
        if(n[k][i]=='I'){
            count+=1;
        }
        else if(n[k][i]=='V'){
            count+=5;
        }
        else if(n[k][i]=='X'){
            count+=10;
        }
        else if(n[k][i]=='L'){
            count+=50;
        }
        else if(n[k][i]=='C'){
            count+=100;
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

void trans(int ans[],int i){
    if(ans[i]==3000){
        printf("MMM");
    }
    else if(ans[i]==2000){
        printf("MM");
    }
    else if(ans[i]==1000){
        printf("M");
    }
    else if(ans[i]==900){
        printf("CM");
    }
    else if(ans[i]==800){
        printf("DCCC");
    }
    else if(ans[i]==700){
        printf("DCC");
    }
    else if(ans[i]==600){
        printf("DC");
    }
    else if(ans[i]==500){
        printf("D");
    }
    else if(ans[i]==400){
        printf("CD");
    }
    else if(ans[i]==300){
        printf("CCC");
    }
    else if(ans[i]==200){
        printf("CC");
    }
    else if(ans[i]==100){
        printf("C");
    }
    else if(ans[i]==90){
        printf("XC");
    }
    else if(ans[i]==80){
        printf("LXXX");
    }
    else if(ans[i]==70){
        printf("LXX");
    }
    else if(ans[i]==60){
        printf("LX");
    }
    else if(ans[i]==50){
        printf("L");
    }
    else if(ans[i]==40){
        printf("XL");
    }
    else if(ans[i]==30){
        printf("XXX");
    }
    else if(ans[i]==20){
        printf("XX");
    }
    else if(ans[i]==10){
        printf("X");
    }
    else if(ans[i]==9){
        printf("IX");
    }
    else if(ans[i]==8){
        printf("VIII");
    }
    else if(ans[i]==7){
        printf("VII");
    }
    else if(ans[i]==6){
        printf("VI");
    }
    else if(ans[i]==5){
        printf("V");
    }
    else if(ans[i]==4){
        printf("IV");
    }
    else if(ans[i]==3){
        printf("III");
    }
    else if(ans[i]==2){
        printf("II");
    }
    else if(ans[i]==1){
        printf("I");
    }
}


int main(){
    int R[10]={1000,100,10,1};
    char n[2][1000];
    int temp1,temp2;
    int a;
    int ans[1000];

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
            for(int i=0;i<4;i++){
                if(a/R[i]>=1){
                    ans[t]=(a/R[i])*R[i];
                    a=a-ans[t];
                    t++;
                }
            }
        }
        for(int i=0;i<t;i++){
            trans(ans,i);
        }
        printf("\n");
    }
    return 0;
}
