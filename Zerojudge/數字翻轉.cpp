#include <bits/stdc++.h>
using namespace std;


int main(){
    string num;
    cin >> num;
    int lens=num.length();
    int mid=lens/2;
    int j=lens-1;
    char temp;
    int count=0;

    if(num[0]=='0'){
        printf("0");
    }

    for(int i=0;i<mid;i++){
        temp=num[i];
        num[i]=num[j];
        num[j]=temp;
        j--;
    }
    
    if(num[0]=='0'){
        for(int i=0;i<lens;i++){
            if(num[i]=='0'){
                count++;
            }
            else{
                break;
            }
        }
        for(int j=count;j<lens;j++){
            printf("%c",num[j]);
        }
    }
    
    else{
        cout << num << endl;
    }
    return 0;
}