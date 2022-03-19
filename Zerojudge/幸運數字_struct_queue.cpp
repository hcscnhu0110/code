#include <bits/stdc++.h>
using namespace std;

struct thing{
    int num;
    int site;
};

bool mycompare(thing a,thing b){
    return a.num < b.num;
}

int smaller(queue<int> temp){
    int a=temp.front();
    int count=0;
    while(1){
        temp.pop();
        int b=temp.front();
        count++;
        if(a > b){
            break;
        }
    }
    return count;
}

int bigger(queue<int> temp){
    int a=temp.front();
    int count=0;
    while(1){
        temp.pop();
        int b=temp.front();
        count++;
        if(a < b){
            break;
        }
    }
    return count;
}

int new1[300010],new2[300010];

void judge(int a[],int n,int start,queue<int> temp){
    long long int sum1=0,sum2=0;
    int count1=0,count2=0;

    for(int i=0;i<=start-1;i++){
        sum1 += a[i];
        new1[count1] = a[i];
        count1++; 
    }
    for(int i=start+1;i<n;i++){
        sum2 += a[i];
        new2[count2] = a[i];
        count2++;
    }
    if(sum1 > sum2){
        n=count1;
        if(n != 1){
            int cnt1 = smaller(temp);
            for(int i=0;i<cnt1;i++){
                temp.pop();
            }
            start=temp.front();
            judge(new1,n,start,temp);
        }
        else{
            cout << new1[0];
        }
    }
    else if(sum1 < sum2 || sum1 == sum2){
        n=count2;
        if(n != 1){
            int cnt2 = bigger(temp);
            for(int i=0;i<cnt2;i++){
                temp.pop();
            }
            start=temp.front();
            judge(new2,n,start,temp);
        }
        else{
            cout << new2[0];
        }
    }
}

int main(){
    int n;
    cin >> n;
    thing a1[n];
    int a[n];
    int start;
    queue<int> temp;

    
    for(int i=0;i<n;i++){
        cin >> a[i];
        a1[i].num = a[i];
        a1[i].site = i;   
    }
    sort(a1,a1+n,mycompare);
    for(int i=0;i<n;i++){
        temp.push(a1[i].site);
    }
    start = a1[0].site;
    judge(a,n,start,temp);
    return 0;
}