#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int input[100];
    queue<int> a;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> input[i];
        a.push(input[i]);
    }
    if(input[1] > input[0]){
        a.pop();
    }
    int lens=a.size();
    for(int i=0;i<lens;i++){
        cout << a.front() << " ";
        a.pop();
    }
}