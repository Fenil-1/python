num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)

set=set(l1)
l2=list(set)
print(f"Duplicate items removed :{l2}")