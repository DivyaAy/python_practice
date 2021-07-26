s1 = int(input("enter a number: "))
s2 = int(input("enter a number: "))
s3 = int(input("enter a number: "))
if (s1<s2) and (s1<s3):
    print("the smallest no : ",s1)
elif(s2<s3) and (s2<s1):
    print("s2 is smallest no: ",s2)
else:
    print(s3)

ls = [2,42,55,22,64]
print("the smallest from list: ",min(ls))