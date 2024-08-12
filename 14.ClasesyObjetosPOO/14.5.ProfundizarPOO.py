class fabricaTelefonos(): #Cuando hablamos de self sirve para englovar atributos de nivel de clase 
    def __init__(self,marca,*colores,**modelos): #  *es para tuplas () y **es para diccionario[]
        self.marca =marca
        self.colores =colores
        self.modelos =modelos

telefono =fabricaTelefonos("Alcatel","Negro","Azul","Rojo", m1=500,m2=200) # "Alcatel" es para marca el otro "" despues de Alcatel es para tuplas y si solo pones el dato es diccionario
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria=512 #Atributo temporal

print(telefono.memoria)