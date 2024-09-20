num=int(input("Enter the number of integers you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
k=int(input("enter how much you wnat to move the list to left"))
for i in range(k):
    l1.append(l1[0])
    l1.remove(l1[0])
print(l1)
