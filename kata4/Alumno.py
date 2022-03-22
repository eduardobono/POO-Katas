# Autor: Jose
# version: 0.0.1
# data: 15/03/2022

# description: kata III - sesión de clase

class Alumno():
    # Atributos de clase
    nombre: str
    apellidos: str
    __dni: str
    edad: int
    notas = []
    asignaturas = []

    # Constructor de clase
    def __init__(self, newNom, newApe, newDni, newEdad): # Atributos de instancia
        self.nombre = newNom
        self.apellidos = newApe
        self.__dni = newDni
        self.edad = newEdad
        self.notas = []
        self.asignaturas = []

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