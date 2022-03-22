from kata6.Animal import Animal
from kata6.Mascota import Mascota
from kata6.Perro import Perro

if __name__ == '__main__':

    an1 = Animal('Perro')
    ma1 = Mascota('Tobby')
    pe1 = Perro('chigugua', an1.especie, ma1.nombre)

    print(an1)
    print(ma1)
    print(ma1.nombre)
    print(pe1)
