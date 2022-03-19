#include <bits/stdc++.h>
using namespace std;

void swap(int* a,int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    int a[10]={0};
    int temp;
    int count=0;
    for(int i=0;i<5;i++){
        for(int j=0;j<3;j++){
            cin >> a[j];
            if(j != 0 && a[j] < a[j-1]){
                swap(&a[j],&a[j-1]);
            }
        }
        if(a[0] + a[1] > a[2]){
            count++;
        }
    }
    cout << count;
    return 0;
}