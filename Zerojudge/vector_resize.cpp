#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> a;
    int input;
    int n;
    cin >> n;
    a.resize(5); //(5,10)代表初始化為10,沒寫代表0
    for(int i=0;i<n;i++){
        cin >> a[i]; //vector中前五項已經有值為0,因此可以這樣修改,若要新增第六個值要push_back
    }
    for(const auto &s : a){
        cout << s << " ";
    }
}


