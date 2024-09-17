str=input("Enter a sentence : ")
l1=str.split()

l1.reverse()
for i in range(len(l1)):
    print(l1[i] , end=" ")
