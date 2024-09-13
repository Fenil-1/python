income=int(input("Enter your incomr to calculate tax : "))
if income<0:
    print("ops invalid income")
elif income<=10000:
    tax=(0.1)*income
    print("Tax will be :" , tax)

elif income>=10001 and income<=50000:
    income=income-10000
    tax1=1000
    tax2=(0.2)*income
    tax=tax1+tax2
    print(f"Tax will be {tax}")

elif income>50000:
    income=income-50000
    tax1=10000
    tax2=(0.3)*income
    tax=tax1+tax2
    print(f"Tax will be {tax}")



