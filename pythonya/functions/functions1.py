"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones.
"""
def presentacion():
    print('Bienvenido al programa')


def carga_suma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print("El resultado de la suma es " + str(suma))

def finalizacion():
    print("El programa ha finalizado")
presentacion()
carga_suma()
finalizacion()


"""
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
"""

def carga_suma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    print("El resultado de la suma es " + str(valor1 + valor2))
    


for i in range(5):
    carga_suma()
    print("-----------------------------------------------")