#Crear un programa que pida al usuario una letra, y si es vocal,
#muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal


letra = input("Ingrese una vocal: ")

if letra.lower() in("aeiuo"):
    print("Es una vocal")
else:
    print("No es una vocal")




