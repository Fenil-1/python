str=input("Enter string to count vowels : ")
count=0
for i in range(len(str)):
    if str[i] in "aeiou":
        count+=1
    else:
        continue
    
print("The total number of vowels in the given string:", count)
