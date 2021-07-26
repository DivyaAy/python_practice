def odd_even(a,b):
    if (num1%2==0) or (num2%2==0):
        even.append(num1)
        odd.append(num2)
    else:
        odd.append(num1)
        even.append(num2)
    #if (num1%2==0):
        #even.append(num1)
        #even.append(num2)
        
    #elif(num2%2==0):
        #odd.append(num1)
        #odd.append(num2)
        #even.append(num2)
    #else:
        #print("it is odd number")


num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
even = []
odd = []
odd_even(num1,num2)
print(even)
print(odd)