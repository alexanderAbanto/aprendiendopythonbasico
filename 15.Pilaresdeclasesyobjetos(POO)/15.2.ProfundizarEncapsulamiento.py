class A():
    def __init__(self):
        self._contador = 0#_encapsulamos de forma correcta y se utiliza en diferenets atributos
        self.cuenta=0

    def increment(self):
        self._contador += 1

        def cuenta(self):
            return self._contador #El _ va a a avisar a otro programador que es un atributo encapsulado 

a=A()     
  


#print(a.cuenta) Esto no se usa de esta manera
#a.cuenta=20 Esto no se usa de esta manera
#print(a.cuenta) Esto no se usa de esta manera