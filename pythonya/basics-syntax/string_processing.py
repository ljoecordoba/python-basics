#Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen.

nombre = input("Ingrese nombre: ")
print("Primer caracter: "  + nombre[0])
print("Cantidad de caracteres: "  + str(len(nombre)))


#Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

if nombre[0] in 'aeiou':
    print("El nombre comienza con vocal")
else:
    print("El nombre no comienza con vocal")
    
