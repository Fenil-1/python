num=int(input("Enter the number of integers you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)

num1=int(input("Enter the number of integers you want to add: "))
l2=[]
for i in range(num1):
    push=int(input("Enter to append: " ))
    l2.append(push)
print(l1)
print(l2)

req=int(input("Enter the number of element you want :"))
# for f in range(1,1+len(l1)+len(l2)):
if req<len(l1):
    print(l1[req-1])
elif req>len(l1):
    print(l2[req-len(l1)-1])
elif req==len(l1):
    print(l1(-1))