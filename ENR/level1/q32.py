import math
num=int(input("enter a numbe"))
a= math.sqrt(num)
b=math.floor(a)
count=0
for i in range(2,b+1):
    if num%i == 0:
        count+=1

if count>=1:
    print("the number is not prime")
else:
    print("the numbe is prime")