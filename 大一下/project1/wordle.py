import random
import os

class color:
    green = '\033[92m'
    yellow = '\033[93m'
    reset = '\033[0m'

def change_green(alpha):
    alpha = color.green + " " + alpha + color.reset 
    return alpha

def change_yellow(alpha):
    alpha = color.yellow + " " + alpha + color.reset 
    return alpha

with open('voc.txt','r',encoding = 'utf-8') as f:
    l = f.readlines()
print("Please input the length you want:")
word_length = int(input())
while True:
    s = random.choice(l)
    if len(s) == word_length+1:
        break
print(s,end = "")

print("Start:")
while True:
    try:
        x = input()
        for i in range(len(s)-1):
            if x[i] == s[i]:
                print(color.green + x[i] + color.reset,end = '')
            else:
                print(x[i],end = '')
        os.system('cls||clear')
        print()
    except:
        break