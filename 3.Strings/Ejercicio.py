#Ejercicio 1
#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
#•Imprima los dos primeros caracteres.
#•Imprima los tres últimos caracteres.
#•Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
#•Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
#•Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
saludo = "Te quiero solo como amigo"
print(saludo[0:2]) #primeros 2 caracteres
print(saludo[-3: ]) #los 3 ultimos
print(saludo[::2]) #cada 2 espacios lo omite
print(saludo[::-1]) #te escribe  a la inversa
print(saludo + saludo[::-1]) #texto normal con texto a la inversa
print(saludo.swapcase())

#Ejercicio 2
#Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r
#Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
palabra = "eparado"
cadena ="Este es el uso del metodo replace"
print(cadena)
reemplazar = cadena.replace("e","E") #Reemplaza la letra e por E
print(reemplazar)

print(palabra)
reemplazar=palabra.replace("",",")#Reemplazamos el espacio entre letras por comas
print("s",reemplazar)

