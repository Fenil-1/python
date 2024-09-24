def is_power_of_three(n):
    if n == 1:
        return True
    if n < 1:
        return False
    # Recursive case
    return is_power_of_three(n / 3)
#test\/
inp=int(input("Enter to check the power of three"))
print(is_power_of_three(inp))

