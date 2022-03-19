n = int(input())
N = n
for i in range(n):
    for j in range(N,0,-1):
        print('*',end = '')
    print()
    N-=1
