str = input("Enter a number: ")
num_digits = len(str)
sum = 0
for digit in str:
    sum += int(digit) ** num_digits
if sum == int(str):
    print(f"{int(str)} is an Armstrong number.")
else:
    print(f"{int(str)} is not an Armstrong number.")
