x = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    try:
        trans = list()
        A,b = map(int,input().split())
        if A < b:
            print (x[A])
            continue
        else:
            while A >= b:
                trans.append(A%b)
                A = A//b
                if A < b:
                    trans.append(A)
            trans.reverse()
        for i in trans:
            print(x[i],end = '')
        print()
    except:
        break