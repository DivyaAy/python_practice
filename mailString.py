import smtplib as sm
even=[]
for i in range(10):
    n = int(input("enter a numnber: "))
    if n%2==0:
        even.append(n)
print(even)
int_str = [str(x) for x in even]
print(int_str)
y = "".join(int_str)

connection=sm.SMTP("smtp.gamil.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedivya1998@gmail.com","amarthiga@gmail.com",y)
print("Email has sent successfully")
connection.quit()