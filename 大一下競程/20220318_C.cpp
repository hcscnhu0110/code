#include <bits/stdc++.h>
using namespace std;
typedef long long int llint;

bool cmp(pair<llint,llint>a , pair<llint,llint>b){
    return a.second < b.second;
}

int main(){
    int T;
    int N;

    cin >> T;
    for(int i=0;i<T;i++){
        int flag = 0;
        cin >> N;
        pair<llint,llint> td[N];
        for(int j=0;j<N;j++){
            cin >> td[j].first;
        }
        for(int j=0;j<N;j++){
            cin >> td[j].second;
        }
        sort(td,td+N,cmp);
        for(int j=0;j<N;j++){
            llint time = 0;
            for(int k=0;k<=j;k++){
                time += td[k].first;
            }
            if(time > td[j].second){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            cout << "Yes" << "\n";
        }
        else{
            cout << "No" << "\n";
        }
    }
}