#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    string mos;
    string s;
    map<string,string> m;
    map<string,string> :: iterator it;
    m[".-"] = 'A';
    m["-..."] = "B";
    m["-.-."] = "C";
    m["-.."] = "D";
    m["."] = "E";
    m["..-."] = "F";
    m["--."] = "G";
    m["...."] = "H";
    m[".."] = "I";
    m[".---"] = "J";
    m["-.-"] = "K";
    m[".-.."] = "L";
    m["--"] = "M";
    m["-."] = "N";
    m["---"] = "O";
    m[".--."] = "P"; 
    m["--.-"] = "Q";
    m[".-."] = "R";
    m["..."] = "S";
    m["-"] = "T";
    m["..-"] = "U";
    m["...-"] = "V";
    m[".--"] = "W";
    m["-..-"] = "X";
    m["-.--"] = "Y";
    m["--.."] = "Z";

    cin >> n;
    cin.ignore();
    for(int i=0;i<n;i++){
        getline(cin,mos);
        stringstream ss(mos);
        while(ss >> s){
           it = m.find(s);
           if(it != m.end()){
               cout << it -> second;
           }
        }
        cout << endl;
    } 
}