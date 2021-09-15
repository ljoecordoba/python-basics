"""
Problema 1:

Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Cliente y la clase Banco.

Luego debemos definir los atributos y los métodos de cada clase:
"""


class Cliente():
    def __init__(self,nombre,monto):
        self.nombre = nombre
        self.monto = monto
    def depositar(self,monto):
        self.monto += monto
    def extraer(self,monto):
        self.monto = self.monto - monto
    def get_monto(self):
        return self.monto
    
    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

    

class Banco():

    def __init__(self):
        self.clientes = []
        self.clientes.append(Cliente("Roque Perez", 23999))
        self.clientes.append(Cliente("Laura Gomez", 20111))
        self.clientes.append(Cliente("Alvear",20))
    def calcular_dinero_total(self):
        total = 0
        for i in self.clientes:
            total += i.get_monto()
        return total
    
banco = Banco()
total = banco.calcular_dinero_total()
print(total)

"""
Problema 2:
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Dado y la clase JuegoDeDados.

Luego los atributos y los métodos de cada clase:
"""
import random


class Dado():

    def tirar(self):
        self.valor=random.randint(1,6)

    def imprimir(self):
        print("Valor del dado:",self.valor)

    def retornar_valor(self):
        return self.valor
class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Gano")
        else:
            print("Perdio")

# bloque principal del programa

juego_dados=JuegoDeDados()
juego_dados.jugar()