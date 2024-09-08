sentence=input("Enter a sentence :")
list=sentence.split(" ")


count=0
max=0
for i in range(len(list)):
    count=len(list[i])
    if max>=count:
        max=max
    else:
        max=count


for j in range(len(list)):
    if max==len(list[j]):
        print(f"The largest word in the sentence is {list[j]}.")
        break