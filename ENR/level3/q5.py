num=int(input("enter till you want to print fabonacci "))
p1=1
p2=0
print(1)
even=0
for i in range(num):
    sum=p1+p2
    print(sum,end=" ")
    p2=p1
    p1=sum
    if sum%2==0:
        even+=sum
print(f"the sum of even numbers in the series is {even}")