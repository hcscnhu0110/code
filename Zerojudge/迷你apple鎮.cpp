#include <bits/stdc++.h>
using namespace std;

struct thing{
    int f,f1;
};

bool compare(thing a,thing b){
    return a.f1 < b.f1;
}

int main(){
    int n;
    int input;
    int count=0;
    cin >> n;
    thing num[n];

    for(int i=0;i<n;i++){
        cin >> num[i].f;
        if(num[i].f < 0){
            int x=0-num[i].f;
            num[i].f1 = num[i].f + x*2;
        }
        else{
            num[i].f1 = num[i].f;
        }
    }
    sort(num,num+n,compare);
    for(int i=0;i<n-1;i++){
        if(num[i].f > 0 && num[i+1].f < 0){
            count++;
        }
        else if(num[i].f < 0 && num[i+1].f > 0){
            count++;
        }
    }
    cout << count;
    return 0;
}