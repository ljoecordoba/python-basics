#Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

mail = input("Ingrese un mail: ")
cantidad = 0
indice = 0

while indice < len(mail):
    if mail[indice] == '@':
        cantidad +=1
    indice +=1

if cantidad == 1:
    print("Contiene un solo caracter @ el mail ingresado")
else:
    print("Incorrecto")
        