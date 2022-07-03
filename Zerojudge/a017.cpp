#include <bits/stdc++.h>
using namespace std;

int judge(char c){
    char op[7] = {'+', '-', '*', '/', '%', '(', ')'};
    int priority[7] = {1, 1, 2, 2, 3, 3};
    for(int i = 0; i < 7; i++){
        if(c == op[i]){
            return priority[i];
        }
    }
    return -1;
}

void infix_to_postfix(string token, stack<char> &op, queue<string> &postfix){
    if(judge(token[0]) == -1){
        postfix.push(token);
    }
    else{
        if(token[0] == '('){
            op.push(token[0]);
        }
        else if(token[0] == ')'){
            while(op.top() != '('){
                string tmp(1, op.top());
                postfix.push(tmp);
                op.pop();
            }
            op.pop();
        }
        else if(op.empty() || judge(token[0]) > judge(op.top())){
            op.push(token[0]);
        }
        else if(judge(token[0]) <= judge(op.top())){
            while(!op.empty() && op.top() != '('){
                string tmp(1, op.top());
                postfix.push(tmp);
                op.pop();
            }
            op.push(token[0]);
        }
    }
}

void calculate(queue<string> &postfix){
    stack<long long int> result; 
    while(!postfix.empty()){
        if(isdigit(postfix.front()[0])){
            stringstream str_to_int;
            long long int tmp;
            str_to_int << postfix.front();
            str_to_int >> tmp;
            result.push(tmp);
        }
        else{
            char op = postfix.front()[0];
            long long int a, b, ans;
            b = result.top();
            result.pop();
            a = result.top();
            result.pop();
            switch (op){
                case '+' :
                    ans = a + b;
                    break;
                case '-' :
                    ans = a - b;
                    break;
                case '*' :
                    ans = a * b;
                    break;
                case '/' :
                    ans = a / b;
                    break;
                case '%' :
                    ans = a % b;
                    break;
            }
            result.push(ans);
        }
        postfix.pop();
    }
    cout << result.top() << endl;
}

int main(){
    string infix;
    stack<char> op;
    queue<string> postfix;
    while(getline(cin, infix)){
        stringstream ss(infix);
        string token;
        while(getline(ss, token, ' ')){
            infix_to_postfix(token, op, postfix);
        }
        while(!op.empty()){
            string tmp(1, op.top());
            postfix.push(tmp);
            op.pop();
        }
        calculate(postfix);
    }
}