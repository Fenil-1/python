num=int(input("Enter the number of numbers you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)

for j in range(len(l1)-1):
    if l1[j]>l1[j+1]:
        store=l1[j]
    else:
        store=l1[j+1]
print(store)