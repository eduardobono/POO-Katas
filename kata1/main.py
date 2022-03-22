'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###                  Kata 1                ###
        ##############################################
'''

from kata1.Alumno import Alumno

if __name__ == '__main__':
    al1 = Alumno('Juan', 'Perez', '000000000A', 28)

    al1.addNota(9)
    al1.addNota(5)
    al1.addNota(7)
    al1.addAge()

    print(al1)