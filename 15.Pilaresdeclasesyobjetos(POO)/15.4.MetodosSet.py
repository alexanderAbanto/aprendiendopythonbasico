#Get = obtener   y    set = colocar

class A():
    def __init__(self):
        self._cuenta =0 #el _ indica atributos encapsulados
        self._contador =0 

    @property #Metodo get que se le llamo como si fuera atrivuto 
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter #Metodo Set coloca un nuevo dato
    def cuenta(self, cuenta):
        self._cuenta = cuenta


    @property#Metodo get que se le llamo como si fuera atrivuto
    def contador(self):
        return self._contador


    @contador.setter
    def contador(self,contador):
        self._contador = contador


a=A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)
a.contador=30
print(a.contador)