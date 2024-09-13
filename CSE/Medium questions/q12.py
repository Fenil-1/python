a=input("Citizenship status(True/False) : ")
citizen=a.lower()
age=int(input("Enter age : "))
if citizen=="true":
    if age>=18 and age<=120:
        print("Yes , eligible to vote ")
    elif age==0 or age>=120:
        print("INVALID AGE")
else:
    print("CANNOT VOTE !!")

