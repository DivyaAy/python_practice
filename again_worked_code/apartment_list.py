class apparments:
    def __init__(self,Block,Floor,Doorno):
        self.B_Block = Block
        self.F_Floor = Floor
        self.D_Doorno = Doorno
        
obj = []
obj.append(apparments("A",9,49))
obj.append(apparments("B",4,25))
print("The Block is :",obj[0].B_Block)
print("The Floor No is: ",obj[0].F_Floor)
print("The Door No is: ",obj[0].D_Doorno)

