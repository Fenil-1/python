num1=int(input("enter one number : "))
num2=int(input("enter two number : "))

if num1>num2:
    remainder=[]
    for i in range(9):
        rem=num1%num2
        num1=num2
        num2=rem
        remainder.append(rem)
        if rem==0:
            print(f"GCD is {remainder[-2]}")
            break
elif num2>num1:
    remainder=[]
    for i in range(9):
        rem=num2%num1
        num2=num1
        num1=rem
        remainder.append(rem)
        if rem==0:
            print(f"GCD is {remainder[-2]}")
            break





