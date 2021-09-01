#Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.


lista = [1,2,3,4,5]
lista.pop(0)
lista.pop(len(lista)-1)
print(lista)

#Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

lista = []
for i in range(10):
    lista.append(int(input("Ingrese un numero: ")))



posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1


print(lista)