class Schools:
    
    def std_in_school(self,st):
        self.st = st
        print("From the std: ",self.st)
   
    def School_First_name(self,name):
        self.name = name
        print("The SChool First is: ",self.name)


MySchool = Schools()
another_school_name = input("enter a school name: ")


first_name = input("enter a name: ")
st_school = int(input("enter a standard: "))
f_n = MySchool.School_First_name(first_name)
s_s = MySchool.std_in_school(st_school)
MySchool.school_name=another_school_name

print("The school name is :",MySchool.school_name)

print(f_n)
print(s_s)

