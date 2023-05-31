"""
EXERCISE TEXTO
para pasar a un funcion
Diseñar un programa que permita ingresar un texto, separarlo mediante la función
split() en una lista y obtener una nueva lista con las palabras ordenadas por el
tamaño de cada cadena.
"""

# texto = input('ingrese un texto')
# otra forma de doc strings aplicado en python

texto_prueba = """Why do we use it?

    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose.
"""


"""
lista_texto = texto_prueba.split(' ')

clean_lista_texto = []

for palabra in lista_texto:

    clean_value = palabra.replace('\n', '')
    clean_lista_texto.append(clean_value)


# aplicando list comprehension

clean_lista_texto = [x for x in clean_lista_texto if x != '']

clean_lista_texto.sort(key=len)

print(clean_lista_texto)

"""

#
# Dicts
# #

"""
Accesos por Key:Value
get | brackets 

"""


"""
Diccionarios son como los objetos en JS, pero no!!! 
por que?? por que no les podes agregar methods, al contrario solo sirve para 
almacenar cosas, tales como todo tipo de dato, entre ellos: 
sí! funciones

Como se accede? Usando dos tipos de metodos principales: .get() y brackets
"""


import json

file=open("./json_files/json_books.json")

book_list = json.load(file)

sample_book = book_list[0]

# print(type(sample_book))

print(sample_book.get('author'))
print(sample_book['language'])

#Que pasa cuando no existe la key??

# print(sample_book['languages'])
# print(sample_book.get('authors','No existe mi hermano! 😣'))


# Recorrer un dict

for col in sample_book:
    print(sample_book.get(col))


# otra forma mas comun de hacer este recorrido: 

for key,value in sample_book.items():
    print(f"{key} : {value}")



# concatenar dicts :

# print( {**sample_book,**{'dato':'added'} })
print( sample_book | {'dato':'added'} )



#
# Tuplas Inmutable
# #

"""
Accesos por Key:Value
get | brackets 

"""

tup1 = ('physics', 'chemistry', 1997, 2000) # es inmutable... como una lista, pero inmutable

print(tup1[0])

try:
    tup1[0] = 'Maths'

except Exception as e:
    print(e)



#
# Set Inmutable
# #

"""
joins subset union intersection diferrence 
"""

Books_ = [
    {
      "author": "Virginia Woolf",
      "country": "United Kingdom",
      "imageLink": "images/to-the-lighthouse.jpg",
      "language": "English",
      "link": "https://en.wikipedia.org/wiki/To_the_Lighthouse\n",
      "pages": 209,
      "title": "To the Lighthouse",
      "year": 1927
    },

    {
      "author": "Virginia Woolf",
      "country": "United Kingdom",
      "imageLink": "images/to-the-lighthouse.jpg",
      "language": "English",
      "link": "https://en.wikipedia.org/wiki/To_the_Lighthouse\n",
      "pages": 209,
      "title": "To the Lighthouse",
      "year": 1927
    },
    
    {
      "author": "Marguerite Yourcenar",
      "country": "France/Belgium",
      "imageLink": "images/memoirs-of-hadrian.jpg",
      "language": "French",
      "link": "https://en.wikipedia.org/wiki/Memoirs_of_Hadrian\n",
      "pages": 408,
      "title": "Memoirs of Hadrian",
      "year": 1951
    }
]


try:
    Books_Set = set(Books_)
except Exception as e:
    print(e)

checker = []

for book in Books_:
    checker.append(tuple(book.items()))

cleaner_list = list(set(checker))

new_book_list = []

for e in cleaner_list:
    categoria = []
    valor = []

    for keys,values in e:

        categoria.append(keys) 
        valor.append(values)

    dict_ = {key: value for key, value in zip(categoria, valor)}
    
    new_book_list.append(dict_)

print(new_book_list)


"""
Extra zip:
zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

>>> list(zip('abcdefg', range(3), range(4)))
[('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(). The i-th element in every tuple comes from the i-th iterable argument to zip(). This continues until the shortest argument is exhausted.

If strict is true and one of the arguments is exhausted before the others, raise a ValueError.
"""


"""
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']

print(zip(categories,objects))

# puedo crear una nueva lista

a_dict = {key: value for key, value in zip(categories, objects)}

print(a_dict)
"""