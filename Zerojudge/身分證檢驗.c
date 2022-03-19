#include <stdio.h>

int judge1(char id){
    char alpha='A';
    int count;
    if(id != 'I' && id != 'O' && id != 'W' && id != 'X' && id != 'Y' && id != 'Z'){
        count=10;
        for(int i=0;i<=21;i++){
            if(id != alpha+i){
                count++;
            }
            else{
                if(count > 17 && count <=23){
                    return count-1;
                }
                else if(count > 24){
                    return count-2;
                }
                else{
                    return count;
                }
            }
        }
    }
    else if(id == 'I'){
        return 34;
    }
    else if(id == 'O'){
        return 35;
    }
    else if(id == 'W'){
        return 32;
    }
    else if(id == 'X'){
        return 30;
    }
    else if(id == 'Y'){
        return 31;
    }
    else if(id == 'Z'){
        return 33;
    }
}

int main(){
    char id1;
    int id2;
    int trans[10];
    int thing1=100000000;
    int thing2=8;
    int temp1,temp2;
    int one;
    int two=0;
    int ans;

    scanf("%c%d",&id1,&id2);
    int result=judge1(id1);
    temp1=result/10;
    temp2=result%10;
    one=(temp2*9)+temp1;
    
    for(int i=0;i<=8;i++){
        trans[i]=id2/thing1;
        if(i < 8){
            two+=trans[i]*thing2;
            thing2--;
        }
        else{
            two+=trans[i];
        }
        id2=id2%thing1;
        thing1=thing1/10;
    }
    
    ans=one+two;
    if(ans%10 == 0){
        printf("real");
    }
    else{
        printf("fake");
    }
    return 0;

}