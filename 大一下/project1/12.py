def aaa(l,i):
    l[i][1] += 1

l = [['a',1],['b',2],['c',3],['d',4]]
x = input()
for i in range(len(l)):
    if x == l[i][0]:
        aaa(l,i)
print(l)
