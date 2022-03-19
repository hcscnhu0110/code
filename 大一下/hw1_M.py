temp = list(input().split())
word = list()
for i in range(len(temp)):
    word.append(temp[i].lower())
word.sort()

for i in range(len(word)):
    n = word[i]
    count = word.count(n)
    if i > 0 and word[i] == word[i-1]:
        continue
    else:
        print(word[i], count)
