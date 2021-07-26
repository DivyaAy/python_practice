class Department:
    def __init__(self,depname):
        self.depname = depname
    def departname(self):
        print(self.depname)
    def add_students(self,name,roll_no,address):
        print(name,roll_no,address)
d = input("enter a department name: ")    
n = input("enter a name: ")
r = int(input("enter a roll number: "))
a = input("enter a address: ")

Dep = Department(d)
Dep.departname()
Dep.add_students(n,r,a)
