n = int(input("Enter an integer: "))
sum = 0
while n > 0:
    digit = n % 10 
    sum += digit  
    n = n // 10  

print(f"The sum of the digits is: {sum}")
