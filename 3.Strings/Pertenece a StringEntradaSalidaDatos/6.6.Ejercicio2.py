#Ejercicio 2
#Hacer un programa que pida al usuario su nombre,
#su edad y su sexo y los muestre de la siguiente forma:
#Te llamas: <nombre>
#Tu edad es: <edad>
#Eres: <sexo>
nombre = input("Ingrese su nombre: ")
edad = int(input ("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo: ")


print("Te llamas: {}".format(nombre))
print ("Tu eddad es: {}".format(edad))
print ("Tu sexo es: {}".format(sexo))
print("Tellamas: {} tu edad es: {} tu sexo es: {}").format(nombre, edad,sexo)