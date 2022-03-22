'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###               Clase Animal             ###
        ##############################################
'''


class Animal():
    especie: str
    peso: float
    altura: float

    def __init__(self, newEspe):
        self.especie = newEspe
        self.peso = 15.6
        self.altura = 35

    def comer(self):
        pass

    def cazar(self):
        pass

    def dormir(self):
        pass

    def __str__(self):
        return f'[{self.especie}, {self.peso}, {self.altura}]'