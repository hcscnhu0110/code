def cmp1(ask,book):
    flag = 0
    for i in range(len(ask)):
        if ask[i] == book[i]:
            flag = 1
        else:
            flag = 0
            break
    return flag

n = int(input())
name = list()
num = list()
name0 = list()
num0 = list()
price = list()
for i in range(n):
    x = input()
    name.append(x)
    x0 = x.lower()
    name0.append(x0)
    num.append(input())
    price.append(int(input()))

cnt = 1

while True:
    try:
        ask0 = input()
        ask = ask0.lower()
        cnt = str(cnt)
        print('case', cnt+':')
        flag = 0
        if ask.isdigit() == False:
            for i in range(len(name0)):
                if cmp1(ask,name0[i]) == 1:
                    flag = 1
                    print(name[i])
                    print(num[i])
                    print(price[i])
                elif cmp1(ask,name0[i]) == 0:
                    continue
        elif ask.isdigit() == True:
            for i in range(len(num)):
                if cmp1(ask,num[i]) == 1:
                    flag = 1
                    print(name[i])
                    print(num[i])
                    print(price[i])
                elif cmp1(ask,num[i]) == 0:
                    continue
        if flag == 0:
            print('NULL')
        cnt = int(cnt)
        cnt +=1
    except:
        break