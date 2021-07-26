class Calculator:

    def addnum(self,a,b):
        return a+b
    def subnum(self,a,b):
        return a-b
    def mulnum(self,a,b):
        return a*b
    def divinum(self,a,b):
        return a/b
    def flodivi(self,a,b):
        return a//b
   
  

    
My_calculator = Calculator()
a = int(input("enter a number: "))
b = int(input("enter a number: "))

addition = My_calculator.addnum(a,b)
print(addition)
subraction = My_calculator.subnum(a,b)
print(subraction)
multiply = My_calculator.mulnum(a,b)
print(multiply)
division = My_calculator.divinum(a,b)
print(division)
floor_div = My_calculator.flodivi(a,b)
print(floor_div)
