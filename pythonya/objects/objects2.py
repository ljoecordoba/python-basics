"""Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. 
En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
"""
class Empleado:
    
    
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.sueldo = int(input("Ingrese el sueldo"))

    def imprimir(self):
        print("Nombre",self.nombre,"Sueldo",self.sueldo)
        
    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")
    def __str__(self):
        return "nombre: " + self.nombre + " sueldo: " +str(self.sueldo)
    

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()


#Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


# bloque principal

punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()