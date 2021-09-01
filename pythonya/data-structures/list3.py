#Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

number_list = [1,2,80,40,33]
greatest = number_list[0]
index = 0
while index < len(number_list):
    if number_list[index] > greatest:
        greatest = number_list[index]
    index +=1
print("El elemento mas grande es " + str(greatest))

#Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)



lowest = lista[0]
index = 0
while index < len(lista):
    if lista[index] < lowest:
        lowest = lista[index]
    index +=1
print("El elemento mas chico es " + str(lowest))