'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###               Clase Leon               ###
        ##############################################
'''

from kata6.Animal import *


class Leon(Animal):
        sexo: str

        def __init__(self, newEsp):
                super().__init__(newEsp)
                self.sexo = 'macho'

        


