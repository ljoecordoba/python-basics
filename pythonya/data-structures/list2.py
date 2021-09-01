#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.
lista = []
for i in range(5):
    numero = int(input("Ingrese un numero"))
    lista.append(numero)
print(lista)


#Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []
flag = False
while not flag:
    numero = int(input("Ingrese un numero"))
    lista.append(numero)
    if numero == 0:
        flag = True
print("Size of the list: " + str(len(lista)))

