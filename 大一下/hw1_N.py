def cheat1(a):
    co = 0
    cx = 0
    for i in range(3):
        for j in range(3):
            if a[i,j] == 'O':
                co += 1
            elif a[i,j] == 'X':
                cx += 1
    if co - cx > 1 or cx - co > 1:
        return 1
    else:
        return 0

def cheat2(a):
    if a[0,0]==a[0,1] and a[0,1]==a[0,2] and a[1,0]==a[1,1] and a[1,1]==a[1,2]:
        return 1
    elif a[0,0]==a[0,1] and a[0,1]==a[0,2] and a[2,0]==a[2,1] and a[2,1]==a[2,2]:
        return 1
    elif a[1,0]==a[1,1] and a[1,1]==a[1,2] and a[2,0]==a[2,1] and a[2,1]==a[2,2]:
        return 1
    elif a[0,0]==a[1,0] and a[1,0]==a[2,0] and a[0,1]==a[1,1] and a[1,1]==a[2,1]:
        return 1
    elif a[0,0]==a[1,0] and a[1,0]==a[2,0] and a[0,2]==a[1,2] and a[1][2]==a[2,2]:
        return 1
    elif a[0,1]==a[1,1] and a[1,1]==a[2,1] and a[0,2]==a[1,2] and a[1,2]==a[2,2]:
        return 1
    else:
        return 0

def lh(a):
    if a[0,0]=='O' and a[0,0]==a[0,1] and a[0,1]==a[0,2]:
        return 1
    elif a[0,0]=='O' and a[0,0]==a[1,0] and a[1,0]==a[2,0]:
        return 1
    elif a[0,0]=='O' and a[0,0]==a[1,1] and a[1,1]==a[2,2]:
        return 1
    elif a[2,2]=='O' and a[2,2]==a[2,1] and a[2,1]==a[2,0]:
        return 1
    elif a[2,2]=='O' and a[2,2]==a[1,2] and a[1,2]==a[0,2]:
        return 1
    elif a[0,2]=='O' and a[0,2]==a[1,1] and a[1,1]==a[2,0]:
        return 1

def yf(a):
    if a[0,0]=='X' and a[0,0]==a[0,1] and a[0,1]==a[0,2]:
        return 1
    elif a[0,0]=='X' and a[0,0]==a[1,0] and a[1,0]==a[2,0]:
        return 1
    elif a[0,0]=='X' and a[0,0]==a[1,1] and a[1,1]==a[2,2]:
        return 1
    elif a[2,2]=='X' and a[2,2]==a[2,1] and a[2,1]==a[2,0]:
        return 1
    elif a[2,2]=='X' and a[2,2]==a[1,2] and a[1,2]==a[0,2]:
        return 1
    elif a[0,2]=='X' and a[0,2]==a[1,1] and a[1,1]==a[2,0]:
        return 1

import numpy as np
s = list()
for i in range(3):
    x = list(input())
    s.append(x)
a = np.array(s)
if cheat1(a) == 1:
    print('Cheat')
elif cheat1(a) == 0:
    if cheat2(a) == 1:
        print('Cheat')
    else:
        if lh(a) == 1:
            print('LH win')
        elif yf(a) == 1:
            print('YF win')
        else:
            print('Tie')