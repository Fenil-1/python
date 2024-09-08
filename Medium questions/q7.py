num=int(input("Enter the number of integers you want to add (ENTER A MISSING NUMBER AS WELL IN THE CONTINUOUS SERIES): "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
start=l1[0]
for i in range(num):
    if start==l1[i]:
        start+=1
    else:
        print("The missing number is ",start)
        break
    
