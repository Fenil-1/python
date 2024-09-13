#pascals triangle
n=int(input("Enter the number of rows : "))
list=[[]]
for i in range(n):
    for j in range(i+1):
        if(j<i):
            if j==0:
                list[i].append(1)
            else:
                list[i].append(list[i-1][j]+list[i-1][j-1])
        elif i==j:
            list[i].append(1)
        
    print()
print(list)