class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()



#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre",self.nombre,"Nota",self.nota)
        
    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")
        
alumno1 = Alumno()
alumno1.inicializar("Gonzalo",12)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno()
alumno2.inicializar("RoquePerez",20)
alumno2.imprimir()
alumno2.mostrar_estado()
