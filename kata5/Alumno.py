'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###               Clase Alumno             ###
        ##############################################
'''

from kata5.Usuario import Usuario

class Alumno(Usuario):
    asignatura: str

    # Constructor de clase
    def __init__(self, newNom, newApe, newAsig):
        super().__init__(newNom, newApe)
        self.asignatura = newAsig


    # Métodos de clase
    def saludar(self):
        print(f'Bienvenido {self.nombre}')

    def addNota(self, newNota):
        if (newNota < 0) or (newNota > 10):
            print('La nota introducida no es valida')
        else:
            self.notas.append(newNota)

    def addAge(self):
        self.edad += 1

    def getNotas(self):
        print(self.notas)

    def addAsignatura(self, newAsign):
        self.asignaturas.append(newAsign)

    def delAsignatura(self, asign):
        self.asignaturas.remove(asign)

    def getAsign(self):
        for asign in self.asignaturas:
            print(asign)


    @property
    def dni(self):
        return self.__dni

    def __str__(self):
        return f'[{self.nombre}, {self.apellidos}, {self.edad}, {self.dni}, {self.notas}, {self.asignaturas}]'