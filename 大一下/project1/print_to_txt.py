l = list()
with open('temp.txt','w',encoding='utf-8') as f:
    while True:
        try:
            x = input()
            l.append(x)
        except:
            print(l,sep = '\n',file = f)
            break