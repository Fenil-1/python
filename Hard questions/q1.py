import math

m=int(input("Enter length of the grid"))
n=int(input("Enter breadth of the grid"))
area=m*n
store=2
answer=area//store

print(f"The maximum number of block of 2x1 can accomodate is {answer}")
