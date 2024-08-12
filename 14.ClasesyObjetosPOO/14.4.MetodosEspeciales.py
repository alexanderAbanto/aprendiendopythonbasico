class fabricaTelefonos():
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
        print("El objeto {} ha sido creado".format(self.marca)) #Le digo que quiero la marca dentro de la clase

    def __str__(self): #Para saber que atributos tiene cuando tenemos lenguaje maquina
        return "El objeto es {}".format(self.marca)


    def __del__(self): #Es para eliminar cuando acabe de cumplir su funcion
        print("El objeto {} ha sido destruido".format(self.marca))


telefono = fabricaTelefonos("Nokia","Negro")#lo llamo fuera de la clase
print(telefono.marca)
print(telefono)