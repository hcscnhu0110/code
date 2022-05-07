class color:
    green = '\033[92m'
    yellow = '\033[93m'
    reset = '\033[0m'

def change_color(a):
    a = color.green+" "+ a + color.reset 
    return a

n,m = map(int,input().split())
o = input()

c = '╠'
d = '╚'
l = list()
for i in range(n):
    if i == 0:
        a = '╔'
    a = a + '═'*3
    if i < n-1:
        a = a + '╦'
    elif i == n-1:
        a = a + '╗'
for i in range(n):
    if i == 0:
        b = '║'
    b = b + change_color(o)
    b = b + ' ║'
for i in range(n):
    c = c + '═'*3
    if i < n-1:
        c = c + '╬'
    elif i == n-1:
        c = c + '╣'
for i in range(n):
    d = d + '═'*3
    if i < n-1:
        d = d + '╩'
    elif i == n-1:
        d = d + '╝'
for i in range(m):
    if i == 0:
        l.append(a)
    l.append(b)
    if i < m -1:
        l.append(c)
    elif i == m - 1:
        l.append(d)
for i in l:
    print(i)