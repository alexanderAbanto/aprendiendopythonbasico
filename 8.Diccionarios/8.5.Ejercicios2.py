#Ejercicio 2
#Con el siguiente diccionario, debes crear un programa
# que pregunte al usuario por un número; el programa debe
# imprimir el jugador al que hace referencia ese número
#{
#    1 : "Casillas", 15 : "Ramos",
#   3 : "Pique", 5 : "Puyol",
#   11 : "Capdevila", 14 : "Xabi Alonso",
#   16 : "Busquets", 8 : "Xavi Hernandez",
#  18 : "Pedrito", 6 : "Iniesta",
#   7 : "Villa"
#}

diccionario = {1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",
11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez",
18 : "Pedrito", 6 : "Iniesta",7 : "Villa"
}

opcionjugador = int(input("Ingresa el numero de jugador: "))
if opcionjugador in diccionario:
    print(diccionario[opcionjugador])
else:
    print("No esta en el diccionario el numero")