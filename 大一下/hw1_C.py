name = list()
while True:
    try:
        name.append(input())
    except:
        name.sort()
        for f in name:
            print(f)
        break