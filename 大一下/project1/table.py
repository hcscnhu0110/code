class color:
    green = '\033[92m'
    reset = '\033[0m'

def change_color(a):
    a = color.green+" "+ a + color.reset 
    return a

q = input()

with open('temp.txt','w',encoding='utf-8') as f:
    f.write('╔'+'═'*3+'╦'+'═'*3+'╗'+'\n')
    x = '║'+ change_color(q)+' ║'+color.green+' A' + color.reset +' ║'
    f.write(x+'\n')
    f.write('╠'+'═'*3+'╬'+'═'*3+'╣'+'\n')
    f.write('║'+color.green+' A' + color.reset +' ║'+color.green+' A' + color.reset +' ║'+'\n') 
    f.write('╚'+'═'*3+'╩'+'═'*3+'╝'+'\n')