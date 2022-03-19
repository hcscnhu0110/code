from decimal import Decimal , ROUND_HALF_UP
x,y,k = map(float,(input().split()))
k1 = int(k) 
place = Decimal(10) ** -k1
temp = x+y
ans = str(temp)
d = Decimal(ans).quantize(place,ROUND_HALF_UP)
print(d)