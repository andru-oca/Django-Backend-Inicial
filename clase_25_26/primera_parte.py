# asignaciones usando el input por medio de la terminal

# asignacion_entrada:str = input("ingrese el valor respectivo:\t")

# print(f"el valor ingresado es ==>  {asignacion_entrada}")

"""
ESTO ES UN COMENTARIO EN BLOQUE
COMO TAMBIEN UN STRING 
"""

# operadores logicos de existencia:
# https://djangocentral.com/display-char-from-a-z/

# validar si el valor existe dentro de un elemento iterable como un str o una lista(parecido al array en JS)


print("h" in "hola mundo")

print("h" not in "hola mundo")

# En python tambien podemos trabajar modularizaciones como en cualquier otro lenguaje de programacion, sin embargo 
# se suele pensarlo como un module, lo cual te permite trabjar de manera más comoda los archivos para que
# podamos debuggear de manera mas amigable y ordenada.
# Es algo que esta bueno ir viendo que todo funciona de la manera similar
# en todos los lenguajes de programacion, y que cada uno tiene su 
# forma amigable de resolver mas que otro

from modules_custom.modulo_parent import IMPORTANT_DATA

print(IMPORTANT_DATA)


