#include <bits/stdc++.h>
using namespace std;

int judge(char c){
    char op[7] = {'+', '-', '*', '/', '%', '(', ')'};
    int priority[7] = {1, 1, 2, 2, 2, 3, 3};
    for(int i=0;i<7;i++){
        if(c == op[i]){
            return priority[i];
        }
    }
    return 0;
}

int main(){
    string infix;
    stack<char> op;            //operator 運算子
    queue<string> postfix;     //用string因為數字可能不是個位數
    while(getline(cin, infix)){
        stringstream ss(infix);
        string token;
        while(getline(ss, token, ' ')){
            if(judge(token[0]) == 0){      //數字
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
                    op.pop();                   //移除 '('
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
                    op.push(token[0]);             //新的放進去         
                }
            }
        }
        while(!op.empty()){
            string tmp(1, op.top());
            postfix.push(tmp);
            op.pop();
        }
        while(!postfix.empty()){
            cout << postfix.front() << " ";
            postfix.pop();
        }
        cout << "\n";
    }
}