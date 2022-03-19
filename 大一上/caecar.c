#include <stdio.h>

int main()
{
    char s[12];
    int i;
    scanf("%s",s);
    for(i=0;i<10;i++)
    {
        int x=s[10]-'0';
        s[i]+=x;
        if(s[i]>'Z')
            s[i]-=26;
        printf("%c",s[i]);
    }
    return 0;
}
