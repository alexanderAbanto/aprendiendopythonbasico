diccionario = {1:2,2:3,3:4}
diccionario2 = {4:5, 6:7}
#print (diccionario)
#diccionario.pop(3)#recibe una clave que va a elinina, aqui el 3:4
#print(diccionario)
#diccionario.clear() #Limpia el diciconario
#print(diccionario)
#print(diccionario.get(2)) #Nos devuelve el valor 3
#diccionario.setdefault(4,5) #agrega unnuevo valor 
#print(diccionario)

diccionario.update(diccionario2)#junta 2 listas
print(diccionario)
diccionario.copy()#Hacen una copia del diccionario
print(diccionario)