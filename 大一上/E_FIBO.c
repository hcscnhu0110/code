#include <stdio.h>

int fatorial(int n){
    if(n==1 || n == 2){
        return 1;
    }
    return fatorial(n - 1) + fatorial(n - 2);
}

int main(){
    int a;

}