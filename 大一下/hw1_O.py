def judge(a,i,j,b):
    if a[i][j] == 'S':
        b[i+1][j-1] += b[i][j]
        b[i+1][j+1] += b[i][j]
    elif a[i][j] == 'R':
        b[i+1][j+1] += b[i][j]
    elif a[i][j] == 'L':
        b[i+1][j-1] += b[i][j]

import numpy as np
N,M,X = map(int,(input().split()))
a0 = list()
for i in range(N):
    x = list(input())
    a0.append(x)
num = list(map(int,input().split()))
a = np.array(a0)
b0 = np.zeros((N+1,M))
b = b0.astype(int)
b[0][X-1] += 1
ans = 0
for i in range(N):
    if i == 0:
        judge(a,0,X-1,b)
        if N == 1:
            for j in range(M):
                b1 = int(b[i+1][j])
                ans += b[i+1][j]*num[j]
        continue
    elif i > 0:
        for j in range(M):
            if b[i][j] > 0:
                judge(a,i,j,b)
        if i == N-1:
            for j in range(M):
                b1 = int(b[i+1][j])
                ans += b[i+1][j]*num[j]
print(ans)

