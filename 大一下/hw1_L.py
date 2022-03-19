def bs(num,ask):
    left = 0
    right = len(num)
    while left < right:
        mid = (left+right)//2
        if num[mid] < ask:
            left = mid + 1
        elif num[mid] > ask:
            right = mid
        elif num[mid] == ask:
            return 1
    return 0

n,q = map(int,input().split())
num = list(map(int,input().split()))
for i in range(q):
    ask = int(input())
    if bs(num,ask) == 1:
        print('Yes')
    elif bs(num,ask) == 0:
        print('No')