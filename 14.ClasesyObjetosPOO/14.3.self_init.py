class fabricaTelefonos():
    marca = "Samsung"



    def ElaborarHuawei(self):
        self.marca="Huawei"


telefono = fabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)

#otras manera es:

class fabricaTelefonos():
    def __init__(self, marca,color):
        self.marca=marca
        self.color=color
        print("Estoy ejecutando el metodo Init, porque se ha creado un nuevo")
    
telefono=fabricaTelefonos("Huawei","Negro")
print(telefono.marca)
print(telefono.color)

