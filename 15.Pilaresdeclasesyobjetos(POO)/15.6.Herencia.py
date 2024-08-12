class animales(): #Clase padre
    def habla(self):
        print("Yo soy un Animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))



class perro(animales): #Clase Hijo que hereda de la clase padre sus datos
    pass #indicamos que no vamos a indicar nada

class Abeja(animales):
    def __init__(sel,animal):
        self.animal = animal

animal = animales() 
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.descripcion()

