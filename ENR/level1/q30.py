num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)

print(f"the last element of list is {l1[-1]}")