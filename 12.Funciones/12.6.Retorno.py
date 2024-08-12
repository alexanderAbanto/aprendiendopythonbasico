def entero():
    print("Este es un dato entero: ")
    return 10
def decimal():
    print("este es un dato decinal: ")
    return 90.99
def frase():
    return "Mi nombre es Alex Abanto"

def asignacion():
    return 1,2,3,4,5

print(entero())
print(decimal())
print(frase())

a,b,c,d,e = asignacion()


print(a)
print(b)
print(c)
print(d)
print(e)