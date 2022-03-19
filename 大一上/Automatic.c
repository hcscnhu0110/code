#include <stdio.h>

const double pi=3.14159265;

int rv(int x,int y,int z){
    return x*y*z;
}

int ra(int x,int y, int z){
    return (x*y+y*z+x*z)*2;
}

double cv(int x,int y){
    return x*x*pi*y;
}

double ca(int x,int y){
    return (x*x*pi*2)+(x*2*pi*y);
}

double bv(int x){
    return (4*pi*x*x*x)/3;
}

double ba(int x){
    return 4*pi*x*x;
}

int main(){
    int a[6]={0};
    int n,m;
    scanf("%d",&n);
    a[0]+=n;
    int lens=0;
    if(n==1 || n==2)
        lens+=4;
    else if(n==3 || n==4)
        lens+=3;
    else if(n==5 || n==6)
        lens+=2;

    for(int i=1;i<lens;i++){
        scanf("%d",&m);
        a[i]+=m;
    }
    if(a[0]==1){
        int result=rv(a[1],a[2],a[3]);
        printf("%d",result); 
    }
    else if(a[0]==2){
        int result=ra(a[1],a[2],a[3]);
        printf("%d",result);
    }
    else if(a[0]==3){
        double result=cv(a[1],a[2]);
        printf("%f",result);
    } 
    else if(a[0]==4){
        double result=ca(a[1],a[2]);
        printf("%f",result);
    } 
    else if(a[0]==5){
        double result=bv(a[1]);
        printf("%f",result);
    } 
    else if(a[0]==6){
        double result=ba(a[1]);
        printf("%f",result);
    }
    return 0;
}