"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
"""

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")



#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.

def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()