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
    def __init__(self, newNombre):
        self.nombre = newNombre
        self.nota: int

    # Métodos de clase
    # add nota
    def addNota(self, newNota):
        if (newNota < 0) or (newNota > 10):
            print('Introduce nota valida')
        else:
            self.notas.append(newNota)

    # Método t string
    def __str__(self):
        return f"['{self.nombre}',{self.nota}]"