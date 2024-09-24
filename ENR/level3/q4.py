def fact(n):
    uf=1
    for i in range(2,n+1):
        uf*=i
    return uf 

def sum_fact(x):
    sum=0
    for i in range(1,x+1):
        sum+=fact(i)
    return sum

#Testing
print(sum_fact(3))