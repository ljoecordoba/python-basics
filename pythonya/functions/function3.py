"""
Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

"""

def retornar_superficie(lado):
    return lado*lado

val = int(input("Ingrese el valor del lado del cuadrado: "))
superficie = retornar_superficie(val)
print("La superficie del cuadrado es ",superficie)
    
#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
