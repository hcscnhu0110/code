#include <stdio.h>
#include <string.h>
#include <math.h>

int one(char a[35]){
    return strlen(a);
}

double two(int x,int y){
    return sqrt(pow(x,2)+pow(y,2));
}

double three(int x,int y,int z){
    return sqrt(pow(x,2)+pow(y,2)+pow(z,2));
}

int main(){
    int t;
    int a;
    char s[35];
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d",&a);
        if(a==1){
            scanf("%s",s);
            int result=one(s);
            printf("%d\n",result);
        }
        if(a==2){
            int x,y;
            scanf("%d %d",&x,&y);
            double result=two(x,y);
            printf("%.9f\n",result);
        }
        if(a==3){
            int x,y,z;
            scanf("%d %d %d",&x,&y,&z);
            double result=three(x,y,z);
            printf("%.9f\n",result);
        }
        
    }
    return 0;
}