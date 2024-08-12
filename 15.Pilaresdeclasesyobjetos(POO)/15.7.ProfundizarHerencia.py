class Animales():
    def __init__(self, nombre):
        self.nombre = nombre
    
class Perro(Animales):
    def _init(self, nombre, sonido):
        super().__init__(nombre) #El super sirve para que se heredo todo de animales
        self.sonido = sonido


    perro= Perro("Firulais", "Guaaoo!")