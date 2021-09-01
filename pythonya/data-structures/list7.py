#Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
#Imprimir sus elementos accediendo de diferentes modos.
lista = [[1,2,3],[4,5,6],[7,8,9]]

print(lista)
print(lista[0])
print(lista[0][0])
for i in range(len(lista[0])):
    print(lista[0][i])

for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j])