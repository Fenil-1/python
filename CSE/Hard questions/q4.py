num=int(input("Enter till you want to print natural numbers)"))
enter=int(input("enter the position of  number you want to print"))
l1=[]
for i in range(1,num+1):
    l1.append(i)
print(l1)

odd=[]

for i in l1:
    if i%2!=0:
        odd.append(i)
for j in l1:
    if j%2==0:
        odd.append(j)

print(f"The {enter} number is : {odd[enter-1]}")

