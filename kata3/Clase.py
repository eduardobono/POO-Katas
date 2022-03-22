'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###                Clase Clase             ###
        ##############################################
'''

class Clase():
    # Atributos de clase
    profesor: str
    alumnos = []
    asignaturas = []

    # Constructor de clase
    def __init__(self, newProf):
        self.profesor = newProf
        self.alumnos = []
        self.asignaturas = []

    # metodos de clase
    def addAlum(self, newAlum):
        self.alumnos.append(newAlum)

    def delAlum(self, alum):
        self.alumnos.remove(alum)

    def addAsig(self, newAsign):
        self.asignaturas.append(newAsign)

    def delAsig(self, asign):
        self.asignaturas.remove(asign)

