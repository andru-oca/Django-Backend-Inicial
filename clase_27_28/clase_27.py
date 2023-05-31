nombre_apellido = "Laura Bermello"

direccion_local = """el local
se encuentra 
en la 
siguiente altura
"""

sad = "🙁"

usuario_mayor = f"Siempre que llueve estoy: {sad}"


texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

if "simplys" in texto :
    print('existe')
else :
    print('no existe')


counter = texto.count('Lorem')

print(type(texto))

print(counter)

"""
● Cadenas de caracteres.
● Métodos de cadenas.
● f-strings
● Índices y slicing (rebanadas).
● Tipo de datos compuestos.
● Listas. Métodos.
● Tipos de datos mutables e inmutables.
● Tuplas, diccionarios, conjuntos
"""



"""
concatenacion
comparacion
longitud
multiplicacion
upper - lower - capitalize
in | not in
min | max
.join(), .split() y .replace() find()
"""


print("hola"=="HOLA")

print(len(texto))

print(len("\n"))

print('Los redonditos de ricota: '+('ji'*3))

print(f"upper->{nombre_apellido.upper()} lower->{nombre_apellido.lower()} capitalize->{nombre_apellido.capitalize()}")

# ------------------------- #

direccion_ip = "198.168.0.1"

# numeros_de_ip = direccion_ip.split('.')

# print(numeros_de_ip)


lista_ips = ["198.128.0.0" ,"198.168.6.1","198.168.5.1","198.168.3.1", "no se cual es su ip"]



for index,ip in enumerate(lista_ips):

    if ip.find('198') == -1:
        print(ip , f'el valor de posicion es: {index}')



#LISTAS #
"""
https://www.w3schools.com/python/python_lists.asp
Accesos por indice
metodos de recorrido FOR  | WHILE
concatenacion de listas
metodos in | not in
metodos append(), pop(), extend(), insert(), remove()
.index(), count() y reverse()
.sort() y clear()
"""


import json

file = open('json_name.json')

diccionario = json.load(file)

lista_names = diccionario['names']


print(lista_names)

print(lista_names[1])


for nombre in lista_names:
    print(f'te sugiero este nombre :{nombre.upper()}')



i = 0

while i < len(lista_names):
    print(lista_names[i])
    i += 1




print(lista_names.count('Sophia'))


lista_names.append('COLOSSO!')

print(lista_names)

elemento_borrado = lista_names.pop()

print(lista_names)
print(elemento_borrado)

lista_names.pop(2)

print(lista_names)

print(['papas', 'mamas'] + [1,2,3])

val1= ['papas', 'mamas']

val2= [1,2,3] 

val3= [*val1, *val2]

print(val3)

val3.extend(['uno','dos', 'tres'])

print( val3 )


# index y sort #

print(val3.index('uno'))


lista_numeros = [1,34,1,4,2,1,6,782,34]

lista_numeros.sort()

print(lista_numeros)

lista_nueva_str = []

for val in val3:
    lista_nueva_str.append(str(val))

lista_nueva_str.sort()

print(lista_nueva_str)

# print(val3)


REBANADO_LIST = lista_nueva_str[:3]
print(REBANADO_LIST)

string= "hola RAFA!"

slice_string = string[-6:]


print(slice_string)

print(string[5:6:1])


print(slice_string)

print(string[string.index('R')])

#-DICCIONARIOS-#

primer_dic= {
    'nombre': 'Nestor',
    "tarjetas": ['visa','platinum'],
    "obser": {1:'data',2:'data:_2'}
}

print(primer_dic['nombre'])

print(primer_dic.get('observaciones','NO exsite!!'))

print(primer_dic.get('obser','NO exsite!!'))


for ele in primer_dic:
    print(primer_dic[ele])


for index,rosa in primer_dic.items():

    print(index , rosa)




print(type(primer_dic))



tupla = (1,2)


print(tupla[0])

# tupla[0] = 10

# tupla.pop()


lista_valores = [1,2,3,3,3,1,2,3,1,1,12,12,2,3,1,13,13]

no_repetidos = set(lista_valores)


print(no_repetidos)




