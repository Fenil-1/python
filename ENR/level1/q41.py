num=int(input("Enter the number fruits you want to add : "))
l1=[]
for i in range(num):
    push=input("Enter to append: " )
    l1.append(push)
print(l1)
print("##### banana , orange or apple presence check !!!!!!! #########33")
if "apple" in l1:
    print("yes apple is present")
elif "orange" in l1:
    print("yes orange is present")
elif "banana" in l1:
    print("yes banana is present")