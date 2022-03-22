'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 20/03/2022  ###
        ###                  Kata 2                ###
        ##############################################
'''

from kata2.Alumno import Alumno
from kata2.Asignatura import Asignatura

if __name__ == '__main__':
    al1 = Alumno('Juan', 'Perez', '000000000A', 28)

    al1.addNota(9)
    al1.addNota(5)
    al1.addNota(7)
    al1.addAge()

    print(al1)

    as1 = Asignatura('ciencias')
    as1.addNota(10)

    as2 = Asignatura('literatura')
    as2.addNota(7)

    as3 = Asignatura('python')
    as3.addNota(7)

    al1.addAsignatura(as1)
    al1.addAsignatura(as2)

    print(al1)