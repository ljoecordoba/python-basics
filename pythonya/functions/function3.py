"""
Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

"""

def retornar_superficie(lado):
    return lado*lado

val = int(input("Ingrese el valor del lado del cuadrado: "))
superficie = retornar_superficie(val)
print("La superficie del cuadrado es ",superficie)
    
#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
def mayor(val1,val2):
    if val1 >= val2:
        return val1
    else:
        return val2


val1 = 2
val2 = 4

print("El mayor numero es ",mayor(val1, val2))

"""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

"""
def largo(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")