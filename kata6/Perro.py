'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###               Clase Perro              ###
        ##############################################
'''

from kata6.Animal import *
from kata6.Mascota import *

class Perro(Animal, Mascota):
    raza: str

    def __init__(self, newNom, newEspe, newRaza):
        Mascota.__init__(self, newNom)
        Animal.__init__(self, newEspe)
        self.raza = newRaza

    def saluda(self):
        pass

    def __str__(self):
        return f'[{self.nombre}, {self.raza}, {self.especie}, {self.peso}, {self.altura}]'



