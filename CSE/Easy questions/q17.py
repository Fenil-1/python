a=input("Enter a string: ")
str=a.lower()
b=input("Enter a substring to check: ")
check=b.lower()
if check in str:
    print("True")
else:
    print("False")