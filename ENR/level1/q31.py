num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)

string=""
for i in range(len(l1)):
    string+=str(l1[i])
print(f"Concentrated string is {string}")