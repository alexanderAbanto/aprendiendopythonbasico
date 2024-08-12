#Ejercicio 2
#Escribe una lista que tenga los números de 1 al 10. 
#Luego, debes hacer que los datos que están en las posiciones
#4, 7 y 9 sean multiplicados por 2; por último,
# mostrar la lista nueva con los nuevos datos

lista = [1,2,3,4,5,6,7,8,9,10]

lista[3]=lista[3]*2 #Numero en la posicion 4
lista[6]=lista[6]*2 #Numero en la posicion 7
lista[8]=lista[8]*2 #Numero en la posicion 9

#o tambien de esta manera
lista[3] *=2 #Multiplica el numero en la posicion 4
lista[6] *=2 #Multiplica el numero en la posicion 7
lista[9] *=2 #Multiplica el numero en la posicion 9


print(lista)