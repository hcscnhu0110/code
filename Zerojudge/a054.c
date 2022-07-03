#include <stdio.h>

int main(){
    char alpha[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int number[26] = {10, 11, 12, 13, 14, 15, 16, 17, 34,
                      18, 19, 20, 21, 22, 35, 23, 24, 25,
                      26, 27, 28, 29, 32, 30, 31, 33};
    int input;
    scanf("%d", &input);

    int x = 100000000;
    int k = 8;
    int sum = 0;
    int check;
    for(int i = 0; i < 9; i++){
        if(i < 8){
            sum += (input / x) * k;
            input = input % x;
            x = x / 10;
            k--;
        }
        else{
            check = input / x;
        }
    }

    int final = 10 - check;
    if(final == 10){
        final = 0;
    }
    
    int new_number[26];
    for(int i = 0; i < 26; i++){
        new_number[i] = number[i] / 10 + number[i] % 10 * 9;
        if((new_number[i] + sum) % 10 == final){
            printf("%c", alpha[i]);
        }
    }
}