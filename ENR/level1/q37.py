age=int(input("Enter your age: "))
if age>0 and age<12:
    print("you are a child")
elif age>=12 and age<=19:
    print("you are a teenager")
elif age>=20 and age<=60:
    print("you are an adult")
elif age>60:
    print("you are a senior citizen")
    