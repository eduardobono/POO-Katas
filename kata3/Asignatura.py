'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###             Clase Asignatura           ###
        ##############################################
'''

class Asignatura():
    # Atributos de clase
    nombre: str
    nota: int

    # Constructor de clase
    def __init__(self, newNom):
        self.nombre = newNom
        self.nota: int

    # Métodos de clase
    def addNota(self, newNota):
        if 0 <= newNota <= 10:
            self.nota = newNota
        else:
            print('Introduce nota válida')

    def __str__(self):
        return f"['{self.nombre}',{self.nota}]"
