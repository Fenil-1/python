num=int(input("Enter the number of data you want to add : "))
dict={}
for i in range(num):
    push=int(input("Enter to append: " ))
    dict[i]=push
print(dict)

sum=0
for j in range(num):
    sum+=dict[j]
print(f"The sum of values : {sum}")