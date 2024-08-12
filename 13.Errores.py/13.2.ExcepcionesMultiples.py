while True:
    try:
        Numero1=int(input("Ingresa un numero:"))
        resultado =100/numero1
        print(resultado)
        break
    except zeroDivisionError:
        print("No se puede dividir entre cero")


while True:
    try:
        edad=int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except valueError:
        print("Has colocado un valor erroneo")