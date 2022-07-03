import re

url = input()
key = re.search("/channel/\S{24}",url)
if  key:
    print(key.group()[9:])
else :
    print('WRONG')