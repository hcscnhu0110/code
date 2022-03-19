a = input()
x = 0
y = 0
for i in range(len(a)):
    if a[i] == 'U':
        y += 1
    elif a[i] == 'D':
        y -= 1
    elif a[i] == 'L':
        x -= 1
    elif a[i] == 'R':
        x += 1
    elif a[i] == 'X':
        break
print(x, y)