#Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. 
#Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
alumnos = []
notas = []
for i in range(3):
    alumnos.append(input("Ingrese el nombre"))
    nota1 = int(input("Ingrese la primera nota"))
    nota2 = int(input("Ingrese la segunda nota"))
    notas.append([nota1,nota2])

for i in range(len(alumnos)):
    print(alumnos[i],notas[i][0],notas[i][1])