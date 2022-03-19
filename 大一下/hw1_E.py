import math

def isPrime(ask):
    n = math.floor(math.sqrt(ask))
    if ask == 1:
        return 0
    for i in range(2,n+1):
        if ask%i == 0:
            return 0
    return 1
    
        

n = int(input())
ask = list(map(int,input().split()))
for i in range(len(ask)):
    if isPrime(ask[i]) == 0:
        print('False')
    else:
        print('True')