class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self): #cuando llame al contador incremente 
        self.contador += 1

    def cuenta(self): #cuando llame a contador me dira su valor
        return self.contador
    

class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self): #cuando llame al contador incremente 
        self.__contador += 1

    def cuenta(self): #cuando llame a contador me dira su valor
        return self.__contador

print("Objeto 2")    
a=A()
print(a.cuenta()) 
a.incrementar()
print(a.cuenta())

print("Objeto 2")
b =B()
print(b.cuenta()) 
b.incrementar()
print(b.cuenta()) 
print(b.__contador) #No se trabaja de esta fomra __
