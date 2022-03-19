from array import array
import numpy as np
n,m,r = map(int,input().split())
N = list()
M = list()
for i in range(n):
    x = list(map(int,input().split()))
    N.append(x)
for i in range(m):
    y = list(map(int,input().split()))
    M.append(y)
N1 = np.array(N)
M1 = np.array(M)
ans = N1.dot(M1)
for i in range(n):
    for j in range(r):
        print(ans[i][j],end=' ')
    print()