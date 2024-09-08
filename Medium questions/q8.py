a=input("Enter a word to check palindrome: ")
b=a.lower()
str=b.replace(" ","")
rev=str[::-1]
if str==rev:
    print("Yes its a palindrome")
else:
    print("No its not a palindrome")
