#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. 
#Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

#Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor 
#debemos intercambiar los nombres para que las listas continúen paralelas (es decir que en los mismos subíndices de cada lista continúe la información relacionada)

nombres = []
notas = []
for i in range(5):
    nombres.append(input("Inserte un nombre: "))
    notas.append(int(input("Inserte la nota: ")))


for i in range(len(notas)):
    for j in range(i,len(notas)):
        if notas[i] < notas[j]:
            temporal_var = notas[i]
            notas[i] = notas[j]
            notas[j] = temporal_var
            temporal_var = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = temporal_var
            
print("Los nombres de los alumnos y las notas")
print(nombres,notas)