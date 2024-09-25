
rows=int(input("enter rows : "))
column=int(input("enter column : "))
p1=1
p2=0
sum=0

for i in range(rows):
    for j in range(column):
        print(sum, end=" ")
        p2=p1
        p1=sum
        sum=p1+p2
    print()