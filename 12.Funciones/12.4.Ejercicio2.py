#Escribir una función que reciba un 
#número entero positivo y devuelva su factorial.


def factorial():
    numero=int(input("Ingresa tu numero positivo"))
    if numero>0:
        factorial = 1
        for i in range(1,numero+1):
            factorial = factorial * i
            print(factorial)
    else:
        print("El numero es negativo y no podemos proceder")

factorial()