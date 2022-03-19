n,q = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
for i in range(q):
    ask = int(input())
    print(h[ask-1])
