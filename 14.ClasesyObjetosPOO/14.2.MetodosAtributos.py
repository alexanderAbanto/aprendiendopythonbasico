class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam=32
    alamcenamiento=128


    def llamar(self,mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.alamcenamiento
print(telefono.marca)
print(telefono.alamcenamiento)

print(telefono.llamar("hola, ¿con quien hablo?"))
telefono.escucharMusica