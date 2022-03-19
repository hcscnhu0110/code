str , key = input().split()
n = len(key)
new = list()
for i in range(len(str)):
    trans = key[i%n].upper()
    new.append(trans)
    b = ord(new[i])
    if str[i].islower() == True:
        a = ord(str[i]) - 32
        temp = a + b -65
        if temp > 90:
            temp = temp - 26
        temp = temp + 32
        ans = chr(temp)
        print(ans,end = '')
    else:
        a = ord(str[i])
        temp = a + b -65
        if temp > 90:
            temp = temp - 26
        ans = chr(temp)
        print(ans,end = '')