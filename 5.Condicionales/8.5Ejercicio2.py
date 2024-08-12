#Ejercicio 2
#Escribir un programa que, dado un número entero,
#muestre su valor absoluto. Nota: para los números
#positivos su valor absoluto es igual al número
#(el valor absoluto de 52 es 52), mientras que, para los negativos,
#su valor absoluto es el número multiplicado por -1
#(el valor absoluto de -52 es 52).
print(abs(-5))# el valor absoluto de un numero negativo es su numero que se transforma a positivo
numero =int(input("Ingresa el numero ENTERO: "))
if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: ".format(numero), abs(numero))

