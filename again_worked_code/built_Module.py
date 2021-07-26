import platform

a = platform.system()
print("the os of system is ",a)
b = platform.processor()
print("the processor of system is ",b)
c = platform.architecture()
print("the platform bit architecture is ",c)
d = platform.machine()
print("the machine type is",d)
e = platform.node()
print("Systems network name: ",e)