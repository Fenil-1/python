import math
final=int(input("Enter the last number you want to print"))
num=int(input("Enter a number you want to divide : "))


for i in range((math.ceil(final/num))):
    new=num*(i+1)
    start=1+(i*num)
    for j in range(1,num+1):
        if i%2==0:
            print(start,end=" ")
            start+=1
        else:
            print(new,end=" ")
            new-=1
            
        
    print()