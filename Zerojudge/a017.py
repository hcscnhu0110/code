try :
    while True :
        print(eval(input().replace('/', '//')))
except EOFError:
    pass