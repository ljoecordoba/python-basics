#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

nombres = []
edades = []
for i in range(5):
    nombres.append(input("Inserte un nombre: "))
    edades.append(int(input("Inserte la edad: ")))

for i in range(len(nombres)):
    if  edades[i] >= 18:
        print(nombres[i])
