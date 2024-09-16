s1=int(input("Enter the sides of traingle : "))
s2=int(input("Enter the sides of traingle : "))
s3=int(input("Enter the sides of traingle : "))
if s1==s2==s3:
    print(f"The triangle is equilateral")
    
elif s1==s2!=s3 or s2==s3!=s1 or s1==s3!=s2:
    print(f"The triangle is isoceles")
else:
    print(f"The triangle is scalene")