'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###              Clase Usuario             ###
        ##############################################
'''

class Usuario():
    # Atributos de clase
    id: str
    nombre: str
    apellidos: str
    email: str

    # Constructor de la clase
    def __init__(self, newNom, newApe):
        self.id = '12345A'
        self.nombre = newNom
        self.apellidos = newApe
        self.email = 'admin@email.com'

    def getNom(self):
        print(f'Bienvenido {self.nombre}')



