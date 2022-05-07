import random
import os
class color:
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    reset = '\033[0m'


def change_color(word_list,now,aim):
    alpha = word_list[now][aim][0]
    if word_list[now][aim][1] == 1:
        new_alpha = color.green + " " + alpha + color.reset
    elif word_list[now][aim][1] == 2:
        new_alpha = color.yellow + " " + alpha + color.reset
    elif word_list[now][aim][1] == 0:
        new_alpha = " " + alpha
    return new_alpha


def table_a(n):
    for i in range(n):
        if i == 0:
            a = '╔'
        a = a + '═'*3
        if i < n-1:
            a = a + '╦'
        elif i == n-1:
            a = a + '╗'
    return a

def table_empty_b(n):
    for i in range(n):
        if i == 0:
            b = '║'
        b = b + '  '
        b = b + ' ║'
    return b

def table_b(n,word_list,now):
    for i in range(n):
        if i == 0:
            b = '║'
        b = b + change_color(word_list,now,i)
        b = b + ' ║'
    return b

def table_c(n):
    for i in range(n):
        if i == 0:
            c = '╠'
        c = c + '═'*3
        if i < n-1:
            c = c + '╬'
        elif i == n-1:
            c = c + '╣'
    return c

def table_d(n):
    for i in range(n):
        if i == 0:
            d = '╚'
        d = d + '═'*3
        if i < n-1:
            d = d + '╩'
        elif i == n-1:
            d = d + '╝'
    return d

def judge_repeat(word,ans):
    current_plural = list()
    current_singular = list()
    for i in range(len(word)):
        count = ans.count(word[i][0])
        if  count >= 2 and word[i][1] == 2 and current_plural.count(word[i][0]) < count:
            for j in range(i+1,len(word)):
                    if word[j][0] == word[i][0] and word[j][1] == 1:
                        current_plural.append(word[j][0])
            if current_plural.count(word[i][0]) < count:
                current_plural.append(word[i][0])
            else:
                word[i][1] -= 2
        elif count >= 2 and word[i][1] == 2 and current_plural.count(word[i][0]) >= count:
            word[i][1] -= 2
        elif count == 1:
            site = ans.find(word[i][0])
            if word[site][0] == ans[site] and i != site:
                word[i][1] -= 2
            else:
                if word[i][0] not in current_singular:
                    current_singular.append(word[i][0])
                elif word[i][0] in current_singular:
                    word[i][1] -= 2



def create_empty_table(chance,table,length):
    for i in range(chance):
        if i == 0:
            table.append(table_a(length))
        table.append(table_empty_b(length))
        if i < chance -1:
            table.append(table_c(length))
        elif i == chance - 1:
            table.append(table_d(length))

def create_new_table(chance,table,length,number_of_attempts,word_list):
    for i in range(chance):
        if i == 0:
            table.append(table_a(length))
        if i < number_of_attempts:
            table.append(table_b(length,word_list,i))
        if i >= number_of_attempts:
            table.append(table_empty_b(length))
        if i < chance -1:
            table.append(table_c(length))
        elif i == chance - 1:
            table.append(table_d(length))

def answer(length,voc):
    while True:
        flag = 0
        result = random.choice(voc)
        if len(result) == length+1:
            for i in range(length):
                if result.count(result[i]) > 2:
                    flag = 1
                    break
            if flag == 0:
                break
    return result

def not_yet(word,alpha_dict):
    for i in range(len(word)):
        alpha_dict[word[i][0]] +=1 
    for i in alpha_dict:
        if alpha_dict[i] == 0:
            print(i.upper(),end = '')
    print()


def run(length,ans,chance):
    table = list()
    alpha_dict = {chr(i) : 0 for i in range(97,123)}
    remaining_chance = chance
    os.system('cls')
    print("Start:")
    for i in alpha_dict:
        print(i.upper(),end = '')
    print()
    create_empty_table(chance,table,length)
    for i in table:
        print(i)

    word_list = list()
    while remaining_chance != 0:
        table.clear()
        INPUT = input()
        guess = INPUT.lower()
        if guess+'\n' not in voc:
            print('Sorry,this word is not avaliable')
            continue
        if len(guess) < length:
            print('Not enough!')
            continue
        elif len(guess) > length:
            print('Too long!')
            continue
        else:
            cnt_green = 0
            remaining_chance -= 1
            number_of_attempts = chance - remaining_chance
            word = list()
            for j in range(length):
                if guess[j] == ans[j]:
                    alp = guess[j]
                    judge = 1
                    temp = [alp,judge]
                    word.append(temp)
                    cnt_green += 1
                elif guess[j] != ans[j] and guess[j] in ans:
                    alp = guess[j]
                    judge = 2
                    temp = [alp,judge]
                    word.append(temp)
                elif guess[j] != ans[j] and guess[j] not in ans:
                    alp = guess[j]
                    judge = 0
                    temp = [alp,judge]
                    word.append(temp)
            judge_repeat(word,ans)
            word_list.append(word)
        if cnt_green == length:
            os.system('cls')
            create_new_table(chance,table,length,number_of_attempts,word_list)
            for i in table:
                print(i)
            print('Congratulation!')
            break
        else:
            os.system('cls')
            not_yet(word,alpha_dict)
            create_new_table(chance,table,length,number_of_attempts,word_list)
            for i in table:
                print(i)
    if remaining_chance == 0 and cnt_green != length:
        print('Correct answer is',color.blue + ans.upper() + color.reset,end='')


print("Please input the length you want:")
length = int(input())
print("How many chances do you want:")
chance = int(input())
with open('voc.txt','r',encoding = 'utf-8') as f:
    voc = f.readlines()
ans = answer(length,voc)
with open('answer.txt','w',encoding = 'utf-8') as f:
    f.write(ans)
run(length,ans,chance)

        