l = list()
with open('temp.txt','w',encoding='utf-8') as f:
    while True:
        try:
            x = input()
            l.append(x)
            l.append('\n')
        except:
            for i in range(len(l)):
                f.write(l[i])
            break