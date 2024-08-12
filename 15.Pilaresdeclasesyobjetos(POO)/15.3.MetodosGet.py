#Get = obtener   y    set = colozar

class A():
    def __init__(self):
        self._cuenta =0 #el _ indica atributos encapsulados
        self._contador =0 

    @property #Metodo get que se le llamo como si fuera atrivuto 
    def cuenta(self):
        return self._cuenta

    @property#Metodo get que se le llamo como si fuera atrivuto
    def contador(self):
        return self._contador
a=A()
print(a.cuenta)
