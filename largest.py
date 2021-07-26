#l1 = [2,3,4,5]
#print(max(l1))
l1 = int(input("enter a number: "))
l2 = int(input("enter a number: "))
l3 = int(input("enter a number: "))
if (l1>l2) and (l1>l3):
    print("the largest no : ",l1)
elif(l2>l3) and (l2>l1):
    print("l2 is largest no: ",l2)
else:
    print(l3)