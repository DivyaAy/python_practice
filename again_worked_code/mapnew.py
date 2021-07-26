l = [ ]
for i in range(10):
    l.append(i)
    #print(l)
def mul(a):
    return a*2
print(list(map(mul,l)))
