#include <stdio.h>

void call(int* a){
    *a=*a*2;
}

int main(){
    int a=2;
    int b=a;
    call(&a);//會直接改主函式中a的值(副函式用int就不用指標)
    printf("%d",a);
}

//會直接改主函式中a的值