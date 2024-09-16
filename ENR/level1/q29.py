num=int(input("Enter the numbers to add : "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
sum=0
for i in range(len(l1)):
    sum+=l1[i]
print(f'The sum of all numbers in list is {sum}')