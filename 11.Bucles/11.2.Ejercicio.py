#Ejercicio 1
#Escribir un programa que pida un numero al usuario y
# muestre las tablas de multiplicar de ese numero

numero = int(input("Ingrese un numero para saber su tabla: "))
i=0
multi =0
while i<=10:
    multi = numero * i
    print("{} x {}={}".format(numero,i,multi))
    i+=1