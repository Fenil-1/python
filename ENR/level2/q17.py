num=int(input("enter : "))
def prime(n):
    count=0
    for x in range(2,n):
        if n%x==0:
            count+=1
    if count==0:
        return n
    



for i in range(2,num+1):
    if prime(i)==i:
        print(prime(i))
