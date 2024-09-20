num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)
# Doubt ???
rem=input("Enter to remove : ")
for i in l1[:]:
    if rem==i:
        l1.remove(i)
print(l1)