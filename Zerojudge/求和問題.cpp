#include <bits/stdc++.h>
using namespace std;

vector<int> num;
vector<int> temp;

void solve(int m,int pivot,int n){
    int sum = 0;
    while(pivot < n){
        for(int i=pivot;i<=pivot;i++){
            temp.push_back(num.at(i));
        }
    }
}

int main(){
    int n,m;
    cin >> n >> m;
    num.resize(n);
    for(int i=0;i<n;i++){
        cin >> num.at(i);
    }
    sort(num.begin(),num.begin()+n);

}