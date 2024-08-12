#Ejercicio 3
#Escribe un programa que pida dos palabras y
# diga si riman o no. Si coinciden las tres
# últimas letras tiene que decir que riman.
# Si coinciden sólo las dos últimas tiene que
# decir que riman un poco y si no, que no riman.
#extraño <---> tamaño
#desligo <---> amigo
#riman <---> cuerpo
#sol <----> lol

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman por que tienen menos de 3 caracteres")
elif palabra1[-3: ] == palabra2[-3: ]:
    print("Las palabras riman")
elif palabra1[-2: ] == palabra2[-2:]:
    print("Las palabras riman un poco")
else:
    print("No riman")
