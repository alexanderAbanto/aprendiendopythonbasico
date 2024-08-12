#Ejercicio 1
#Escribir una tupla con los meses del año, luego, 
# pide al usuario un numero, el que haya ingresado,
# es el mes que debe mostrar en la tupla

tupla=("enero", "febreo", "Marzo", "abril", "mayo","junio"
       "junio", "agosto", "septiembre", "octubre", "noviembre","diciembre")

OpcionMes =int(input("Ingresa el numero de tu mes:"))
OpcionMes -=1 # el mes menos 1 mes

print("Tu mes es: ", tupla[OpcionMes])


#o tambien 
print("El mes correspondiente es: ", tupla[OpcionMes-1])