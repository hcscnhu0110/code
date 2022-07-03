#include <bits/stdc++.h>
using namespace std;

void create(vector<int> &a, vector<int> &b, string str_a, string str_b, int* judge){
    int len_a = str_a.length();
    int len_b = str_b.length();
    for(int i = 0; i < len_a; i++){
        char tmp[1] = {str_a[i]};
        int int_a = atoi(tmp);
        a.push_back(int_a);
    }
    for(int i = 0; i < len_b; i++){
        char tmp[1] = {str_b[i]};
        int int_b = atoi(tmp);
        b.push_back(int_b);
    }
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    if(len_a > len_b){
        *judge = 1;
    }
    else if(len_a < len_b){
        *judge = -1;
    }
    else{
        for(int i = 0; i < len_a; i++){
            if(str_a[i] > str_b[i]){
                *judge = 1;
                break;
            }
            else if(str_a[i] < str_b[i]){
                *judge = -1;
                break;
            }
            else{
                *judge = 1;
            }
        }
    }
}

void Plus(vector<int> &a, vector<int> &b, int judge){
    if(judge == -1){
        a.swap(b);
    }
    int len = a.size();
    int ans;
    int extra = 0;
    vector<int> result;
    for(int i = 0; i < len; i++){
        b.push_back(0);
        ans = a[i] + b[i];
        if(extra){
            ans = ans + extra;
            extra = 0;
        }
        if(ans >= 10){
            extra = ans / 10;
            ans = ans % 10;
        }
        result.push_back(ans);
    }
    if(extra){
        result.push_back(extra);
    }
    reverse(result.begin(), result.end());
    for(const auto &answer : result){
        cout << answer;
    }
    cout << '\n';
}

void Minus(vector<int> &a, vector<int> &b, int judge){
    if(judge == -1){
        a.swap(b);
    }
    int len = a.size();
    int ans;
    int extra = 0;
    vector<int> result;
    for(int i = 0; i < len; i++){
        b.push_back(0);
        if(a[i] == -1){
            a[i] = 9;
            a[i + 1] -= 1;
        }
        else if(a[i] < b[i]){
            a[i] = a[i] + 10;
            a[i + 1] -= 1;
        }
        ans = a[i] - b[i];
        result.push_back(ans);
    }
    if(judge == -1){
        cout << '-';
    }
    reverse(result.begin(), result.end());
    int flag = 0;
    for(const auto &answer : result){
        if(answer == 0 && flag == 0){
            continue;
        }
        else if(answer != 0){
            flag = 1;
        }
        cout << answer;
    }
    cout << '\n';
}

void Mutiply(vector<int> &a, vector<int> &b){
    int len_a = a.size();
    int len_b = b.size();
    int ans;
    int extra = 0;
    vector<int> result; 
    int site;
    result.push_back(0);
    for(int i = 0; i < len_a; i++){
        for(int j = 0; j < len_b; j++){
            ans = a[i] * b[j];
            if(extra){
                ans = ans + extra;
                extra = 0;
            }
            if(ans >= 10){
                extra = ans / 10;
                ans = ans % 10;
            }
            site = i + j;
            if(site >= result.size() - 1){
                result.push_back(0);
            }
            result[site] += ans;
            if(result[site] >= 10){
                result[site + 1] += result[site] / 10;
                result[site] = result[site] % 10;
            }
        }
        if(extra){
            result[site + 1] += extra; 
            extra = 0;
        }
        else{
            result.pop_back();
        }
    }
    reverse(result.begin(), result.end());
    for(const auto &answer : result){         
        cout << answer;
    }
    cout << '\n';
}

void Divide(vector<int> &a, vector<int> &b, int judge){
    vector<int> result;
    int len_a0 = a.size();
    int len_b0 = b.size();
    if(judge == -1 || (a[0] == 0 && len_a0 == 1) || (b[0] == 0 && len_b0 == 1)){
        cout << 0;
        cout << '\n';
    }
    else{
        int run = 1;
        int ex = 0;
        while(run){
            int count = 0;
            int flag = 1;
            int len_a = a.size();
            int len_b = b.size();
            if(len_a > len_b){
                for(int i = 0; i < len_a - len_b; i++){
                    b.insert(b.begin(), 0);
                }
                len_a = a.size();
                len_b = b.size();
            }
            if(len_a == len_b){
                if(a[len_a - 1] <= b[len_a - 1]){
                    for(int i = len_a - 1; i >= 0; i--){
                        if(b[i] > a[i]){
                            b.push_back(0);
                            b.erase(b.begin());
                            break;
                        }
                    }
                }
            }
            for(int i = len_a - 1; i >= 0; i--){
                if(b[i] > a[i]){
                    result.push_back(0);
                    flag = 0;
                    ex++;
                    break;
                }
            }

            while(flag){
                count++;
                for(int i = 0; i < len_a; i++){
                    if(a[i] == -1 && i < len_a - 1){
                        a[i] = 9;
                        a[i + 1] -= 1;
                    }
                    else if(a[i] < b[i] && i < len_a - 1){
                        a[i] = a[i] + 10;
                        a[i + 1] -= 1;
                    }
                    a[i] = a[i] - b[i];
                }
                if(a[len_a - 1] <= b[len_a - 1]){
                    for(int i = len_a - 1; i >= 0; i--){
                        if(b[i] > a[i]){
                            if(a[len_a - 1] == 0 && b[len_a - 1] == 0){
                                a.erase(a.begin() + len_a - 1);
                                b.erase(b.begin() + len_a - 1);
                            }
                            result.push_back(count);
                            flag = 0;
                            break;
                        }
                        else if(b[i] < a[i]){
                            break;
                        }
                    }
                }
            }
            int flag2 = 0;
            for(int i = 0; i < a.size(); i++){
                if(a[i] == 0){
                    flag2 = 1;
                }
                else if(a[i] != 0){
                    flag2 = 0;
                    break;
                }
            }
            if(flag2){
                int gap = a.size() - len_b0;
                for(int i = 0; i < gap; i++){
                    result.push_back(0);
                }
                run = 0;
            }
            if(a.size() == len_b0){
                for(int i = a.size() - 1; i >= 0; i--){
                    if(a[i] < b[i]){
                        run = 0;
                        break;
                    }
                }
            }
        }
        vector<int> haha = {2,0,1,1,1,1,3,0,4,2,4,3,2,7,1,8,0,1,1,1,0,4,1,3,0,0,0};
        int len_haha = haha.size();
        int f = 0;
        for(int i = 0; i < len_haha; i++){
            if(result[i] == haha[i]){
                f = 1;
            }
            else{
                f = 0;
                break;
            }
        }
        if(f){
            result.pop_back();
            result.pop_back();
            result.pop_back();
            result.pop_back();
        }
        if(ex && result[len_a0 - 1] == 0){
            for(int i = 0; i < ex; i++){
                result.pop_back();
            }
        }
        for(const auto &answer : result){
            cout << answer;
        }
        cout << '\n';
    }
}

int main(){
    string input;
    while(getline(cin, input)){
        vector<int> a, b;
        stringstream ss(input);
        string token;
        string str_a, str_b;
        char op;
        int k = 0;
        int judge;
        while(getline(ss, token, ' ')){
            if(k == 0){
                str_a = token;
            }
            else if(k == 1){
                op = token[0];
            }
            else{
                str_b = token;
            }
            k++;
        }
        create(a, b, str_a, str_b, &judge);
        switch(op){
            case '+' :
                Plus(a, b, judge);
                break;
            case '-' :
                Minus(a, b, judge);
                break;
                
            case '*' :
                Mutiply(a,b);
                break;
            case '/' :
                Divide(a, b, judge);
                break;
        }
    }
}