

def max(x):
    max=0
    for i in range(len(x)):
        if x[i]>max:
            max=x[i]
        else:
            max=max
    
    return max

#call
num=int(input("Enter the number of strings you want to add: "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
print(f"MAx number : {max(l1)}")