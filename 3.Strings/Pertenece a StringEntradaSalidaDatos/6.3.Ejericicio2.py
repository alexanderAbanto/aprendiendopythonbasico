#Ejercicio 2
#Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
#Considere:
#PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
#Donde: P1, P2, P3 : Practicas
#PP: promedio de práctica
#PROM: promedio
#EP: examen parcial
#EF: examen final

practica1=float(input("Ingrese la nota de la practica 1: "))
practica2=float(input("Ingrese la nota de la practica 2: "))
practica3=float(input("Ingrese la nota de la practica 3: "))
ExamenParcial=float(input("Ingrese la nota del examen parcial: "))
ExamenFinal=float(input("Ingrese la nota del examen final: "))

PromedioPractica=(practica1 + practica2+ practica3)/3
PromedioFinal=(PromedioPractica+2*ExamenParcial+3*ExamenFinal)/6

print("La nota promedio de practicas es:\n",PromedioPractica, "La nota final: ", PromedioFinal)