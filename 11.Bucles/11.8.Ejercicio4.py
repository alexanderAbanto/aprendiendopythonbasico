#Ejercicio 2
#Pedir al usuario que ingrese 2 numeros,
#después, se debe mostrar el rango de esos 2 números,
#pero, solo imprimiendo los números que sean impares

numero1=int(input("Ingresa el primer numero : "))
numero2=int(input("Ingresa el segundo numero: "))
for i in range(numero1, numero2+1):
    if i % 2==0:
        continue
    print(i)