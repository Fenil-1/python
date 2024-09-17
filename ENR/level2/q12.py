num=int(input("Enter the number of data you want to add : "))
l1=[]
for i in range(num):
    push=int(input("Enter to append: " ))
    l1.append(push)
print(l1)
l2=[]
for i in range(len(l1)):
    if l1[i]>0:
        if l1[i]%2==0:
            l2.append("positive even")
        else:
            l2.append("positive odd")
    if l1[i]<0:
        if l1[i]%2==0:
            l2.append("negative even")
        else:
            l2.append("negative odd")
    if l1[i]==0:
        l2.append("neutral")
print(f"YoU GoT iT RiGhT BaBy {l2}")
    