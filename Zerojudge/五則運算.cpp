#include <bits/stdc++.h>
using namespace std;

vector<string> v;
vector<int> site;
stack<string> cal;


int main(){
    string line;
    getline(cin,line);
    int lens = line.length()/2 + 1;
    string s[lens];
    stringstream ss(line);
    int count1,count2 = 0;

    for(int i=0;i<lens;i++){
        ss >> s[i];
        v.push_back(s[i]);
        if(s[i] == "("){
            count1 += 1;
        }
        else if(s[i] == ")"){
            
        }
        else if(s[i] == "*" || s[i] == "/" || s[i] == "%"){
            count2 += 1;
        }
    }
    
    cout << v.at(0);
}