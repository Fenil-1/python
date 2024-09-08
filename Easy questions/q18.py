num=int(input("Enter the number of numbers you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
sum=0
for j in range(num):
    a=l1[j]
    sum+=a
average=(sum)/num
print("The average of the numbers is", average)
