num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)

for i in range(len(l1)):
    if l1[i]==0:
        l1.remove(l1[i])
        l1.append(0)
print(f"Zero has more value to the end {l1}")
