str=int(input("Enter the number of strings you want to add: "))
l1=[]
for i in range(str):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)
count=0
store=0
for j in range(str):
    count=len(l1[j])

    if store>=count:
        store=store
    else:
        store=count
print("Max numbers of letter in a string is ",store)
