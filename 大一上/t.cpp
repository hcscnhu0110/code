#include <bits/stdc++.h>
using namespace std;

struct table{
    int a, b;
};

table calculate1(table T1, table T2){
    return table{T1.a - T2.a, T1.b - T2.b};
}

table calculate2(table T1, table T2){
    return table{T1.a * T2.a - T1.b * T2.b, T1.a * T2.b + T1.b * T2.a};
}



int main(){
    table T1, T2;
    cin >> T1.a >> T1.b >> T2.a >> T2.b;
    cout << calculate1(T1, T2).a << " " << calculate1(T1, T2).b << endl;
    cout << calculate2(T1, T2).a << " " << calculate2(T1, T2).b << endl;
    return 0;
}