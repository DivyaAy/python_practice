import smtplib
even = []
for x in range(10):
    num = int(input("enter a number: "))
    if num%2==0:
        even.append(num)

print(even)   
output = [str(a) for a in even]
print(output)
l = "".join(output)
#print(str_of_int)
#print(type(str_of_int))

connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedviya1998@gmail.com","amarthiga@gmail.com",output)
print("email has sent successfully")
connection.quit()