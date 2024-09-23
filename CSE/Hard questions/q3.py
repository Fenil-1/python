file = open("largefile.txt" , "r")
# list=file.readlines()
list=[]
for line in file:
    parts=line.split()
    list.append(parts)
print(parts)

print(list)

for i in list:
    sum=0
    for j in range(1,len(i)):
        sum+=int(i[j])
    for k in range(1,len(i)):
        i.remove(i[1])
    i.append(sum)
print(list)

for x in range(2):
    if 
file.close()