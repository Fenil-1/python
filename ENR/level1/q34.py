num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
sum=0
for i in range(len(l1)):
    if l1[i]%2==0:
        sum+=l1[i]
print(f"The sum of even numbers is : {sum}")
