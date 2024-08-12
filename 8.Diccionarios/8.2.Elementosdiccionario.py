diccionario = {"Nombre":"Alex", "Apellido":"Abanto", "Estatura":1.80}

print(diccionario)
print(diccionario.keys()) #Solo me nuestra las llaves que es nombre, apellido, estatura
print(diccionario.values()) #Solo me muestra los valores alex, abanto 1.80
print(diccionario["Estatura"])# me muestra el valor de lo que llame

diccionario["Peso"]="58 kg" #Agrega un nuevo valor
print(diccionario)

diccionario["Nombre"] ="alex"
print(diccionario)