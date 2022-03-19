#include <stdio.h>

int main(){
    int c[30]={0},d[30]={0};
    char e[30];                //c,d管0和1，e管字母
    int n,m;
    int a,b;
    int x;
    int i=0;
    int y=0,z=0;
    scanf("%d %d",&n,&m);
    for(x=0;x<m;x++){
        scanf("%d %d",&a,&b);
        i+=b;
        c[i]=a;
        d[i]=1;
        e[i]=b+64;
        i=0;
    }
    for(i=1;i<=26;i++){
        if(c[i]==1)
            y++;
        if(d[i]==1)
            z++;
    }
    if(z-y==0){
        printf("yaaaa!");
    }
    else{
        for(i=1;i<=26;i++){
            if(c[i]==0 && d[i]==1)
            printf("Fuck my %c\n",e[i]);
        }
    }
    return 0;
}