# Hello World
print("Hola Mundo!")

# funciones
def miFuncion():
    print("Hola Mundo!")
# LLamar
miFuncion()
# Clases
class MyClass:
    # Constructor
    def __init__(self, args):
        self.args = args
    #Funcion de clases
    def funcion(self):
        print("Hola mundo! desde una Clase!")
# Crear
claseins = MyClass("Test")
claseins.funcion()
# Clases hijas
class MyClaseH(MyClass):
    def __init__(self, args):
        super().__init__(args)
        print("Hija!")
claseHins = MyClaseH("Hola")
claseHins.funcion()
# Implements e Import
from abc import ABC, abstractmethod
# Clase Abstacta
class MyClassA(ABC):
    @abstractmethod
    def hola_mundo(self):
        pass
# Implementar clase
class MyClaseI(MyClassA):
    def hola_mundo(self):
        print("Hola mundo desde Clase Implementada!")
claseImp = MyClaseI()
claseImp.hola_mundo()
#Tipo de imports:
import math
print(math.pi)
#import con alias
import numpy as np
arrayT = np.array([1, 2, 3])
#importar todo (no recomendado)
#from math import *

#fors
for i in range(5):
    print("Hola")

for i in range(1, 6):
    print(i)

#for arrays
frutas = ["manzana", "platano", "cereza"]
for fruta in frutas:
    print(fruta)

#for jsons
diccionario = {
    "nombre": "Pepe",
    "edad": "30"
}
for clave in diccionario:
    print(clave, diccionario[clave])
for clave, valor in diccionario.items():
    print(clave, valor)