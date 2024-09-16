num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)

rem=input("Enter to remove : ")
for i in range(len(l1)):
    yo=l1[i]
    if rem==yo:
        l1.remove(yo)
        break
print(l1)