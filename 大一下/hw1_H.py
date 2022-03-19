while True:
    try:
        ans = 0
        score = list(input().split())
        if len(score) == 0:
            continue
        for i in range(len(score)):
            score1 = int(score[i])
            ans += score1
        print(ans)
    except:
        break
