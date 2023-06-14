from oop_pack.Encapsulacion import Persona
from oop_pack.Abstraccion import PersonaAbstracta
from oop_pack.Abstraccion import Jugador

print("PRIMER PASO DE ENCAPSULACION")



mateo = Persona(
    nombre  =   "mateo",
    email   =   "mateo@mail.com",
    nacionalidad    =   "mexico"
)


print(mateo)
mateo.set_dni(19998822)
mateo.set_tramite("gt-123-ade")
print(mateo)

# print("Te permite mostrarlo aunque no es lo más hermoso =>\t",mateo._Persona__dni)
# print(mateo.__dni)


print("HERENCIA--> CASI CASI ABSTRACCION")

mateo_jugador = Jugador(
    nombre  =   "mateo",
    email   =   "mateo@mail.com",
    nacionalidad    =   "mexico",
    status          = True ,
    club    =   "Sacachispas"
)

mateo_jugador.dni = 123

print(mateo_jugador.dni)


"""
ABSTRACCION NO ME PERMITE CREAR 

l_gante = PersonaAbstracta(
    nombre  =   "l-gante",
    email   =   "l.gante@mail.com",
    nacionalidad    =   "argentina"
)


print(l_gante)
"""


print("Poliformismo")

from oop_pack.Polimorfismo import Italiano , Peruano , Brasilero , Argentino


sergio = Italiano(
    nombre  =   "sergio",
    email   =   "serg@mail.com",
    nacionalidad    =   "italiano",
)
sergio.dni      = 999
sergio.tramite  = 123

william = Peruano(
    nombre  =   "william",
    email   =   "will@mail.com",
    nacionalidad    =   "peruano",
)
william.dni     = 888
william.tramite = 23111

boris = Brasilero(
    nombre  =   "boris",
    email   =   "boris@mail.com",
    nacionalidad    =   "brasil",
)
boris.dni       = 777
boris.tramite   = 123123

juan = Argentino(
    nombre  =   "juan",
    email   =   "juan@mail.com",
    nacionalidad    =   "argentino",
)
juan.dni        = 6666
juan.tramite    = 98765


print(sergio.printDNI())




