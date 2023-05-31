# texto = "hola mundo"
# texto_hints:int = "hola mundo con  hints"

# print(texto, "\n" , texto_hints)
# print(texto )


# edad:str = input("ingresa la edad: \n")
# edad:int = int(edad)

# print("la edad ingresada es :\t", edad)

# --------------------------

"""
    esto es un comentario en bloque

    vamos a ver condicionales

    if( condicion ){
        bloque de codigo
    }

"""

# if edad > 50:
#     print("tengo mas de 50")
# elif edad > 18 : 
#     print("soy mayor de edad, wiiii!!")
# else :
#     print("lola!!")

# --------------------------


# quotte = """

#     No podemos estar en modo de supervivencia. Tenemos que estar en modo de crecimiento - Jeff Bezos.

# """
# i = 0

# for char in quotte:
#     i += 1
#     print(i, ' ==>' + char)


"""
for(let i = 0 ; i< numero ; i++){

    bla bla bla
}

"""

# for num in range(0,100,10):
#     print(num)

# edad:str = input("ingresa la edad: \n")
# edad:int = int(edad)


# while edad < 18 :
#     print("sos menor de edad, intenta otra vez")
#     edad:str = input("ingresa la edad: \n")
#     edad:int = int(edad)
# else:
#     print("al fin saliste!!")



# flag  = True

# while flag :
#     edad:str = input("ingresa la edad: \n")
#     edad:int = int(edad)

#     if edad > 18:
#         print("sos mayor de edad")
#         flag = False
# else:
#     print("validamos que sos mayor de edad")



# while True:
   
#     edad:str = input("ingresa la edad: \n")
#     edad:int = int(edad)

#     if edad > 18:
#         print("sos mayor de edad")
#         break

from lorena_const.constantes import UUID
from lorena_const.constantes import OTRO_TIPO
from lorena_const.constantes import saludar

print(UUID)
print(OTRO_TIPO)
print(saludar())
