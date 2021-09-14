"""
Definir por asignación una lista de enteros en el bloque principal del programa. 
Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

"""

def sumar_lista(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return sum

def menor_lista(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor
    
def mayor_lista(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor 

lista = [30,4,50,40,73]
print(sumar_lista(lista))
print(menor_lista(lista))
print(mayor_lista(lista))
