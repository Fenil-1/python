num=int(input("Enter the number of strings you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
l2=[]

for i in range(len(l1)):
    if l1[i]%2==0:
        l2.append(l1[i])
        l2.append((l1[i])**2)
print(l2)
