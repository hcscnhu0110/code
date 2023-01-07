#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char input[1000];
    while(gets(input) != NULL){
        double sum = 0;
        int size = 0;
        const char *delim = " ";
        char *value;
        value = strtok(input, delim);

        int count = 0;
        while(value != NULL){
            sum += atoi(value);
            size++;
            value = strtok(NULL, delim);
        }
        double ave = sum / size;
        printf("Size: %d\n", size);
        printf("Average: %.3f\n", ave);
    }
}