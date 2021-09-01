#Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

list = [1,2,3,4,5]
suma = 0
for i in range(len(list)):
    suma += list[i]
print("La suma de todos los elementos es igual " + str(suma))

#Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año. Mostrar el primer y último elemento de la lista solamente.

list = ['enero', 'febrero', 'marzo', 'abril']

print(list[0])
print(list[len(list)-1])


#Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

lista = ['Maria',7,10]
print('El nombre del alumno/a es : ' + lista[0])
print('El promedio de sus notas es: ' + str((lista[1] + lista[2])/2))