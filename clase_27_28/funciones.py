"""
Funciones!!

Que es una funcion?

Para que sirven?

Que se puede hacer?

Valores por default

Funciones. Concepto.

● Llamada a función.


    Usando las funciones en llamado 


● Retorno y envío de valores.
    Todas las funciones deben devolver algo, si no se le puede considerar como una funcion procedural 

    !! mega curiosidad : ¿Cuando concluye una función?
        Solamente cuando se llega al valor return, de otra forma el ciclo de vida aún se encuentra activo.

    Concepto de funciones puras
    http://www.etnassoft.com/2016/06/21/las-funciones-puras-en-javascript-concepto-ejemplos-y-beneficios/

    En programación, las Funciones Puras son aquellas que cumplen con dos requisitos básicos:

    Dado unos parámetros de entrada de idéntico valor, la función siempre devolverá el mismo resultado.
    El cómputo de la función, su lógica, no implica ningún efecto observable colateral fuera de ella.

    ejemplo de funcion pura 

    def suma_pura(a,b):
        return a+b

    print(suma_pura(1,2))
    print(suma_pura(2,1))


    Por un lado, podemos observar e intuir que siempre que llamemos a esta función con los mismos parámetros, el resultado será idéntico.
    Al no requerir o depender de ningún estado o valor fuera de ella, la salida debe ser siempre la misma para valores dados iguales.
   
    Por otro, el cálculo que realiza nuestra función no modifica durante el mismo nada fuera de ella.
    Eso es extensible a las mismas variables que recibe como entrada: ni a ni b son \'mutadas\' durante el proceso.

● Parámetros, argumentos, valor
y referencia.

    Son los elementos que utilizamos para que la funcion pueda trabajar, no son re requerimiento indispensable
    
    Valor por referencia =  se podrían observar desde el concepto de la ejecución de direccion de la memoria del programa
    en otros lenguajes de programación como C# C++ Golang, tienen puntoreso valores referenciados los cuales hacen referencia al valor de memoria que se encuentra 
    alojada la variable

    data = 'hello'

    #Unico twist que encontré de como hacer un hard copy de un string

    saludo = (data.join(''))[:] #lo que sucede en este caso es que se transforma 

    print(id(data), id(saludo))



    ejemplo
        id(variables)


    Argumentos por default 
        Son los que siempre recomiendo colocar dado a su gran uitilidad no sólo en la hora de trabajar con funciones si no para hacer que el usuario
        maneje los valores de entrada nula y evita errores en la forma de como trabaja la función sin estados inicializados



● Parámetros mutables e
inmutables.




    ARGS y KWARGS
    Con que se come esto??
    Bueno es el concepto de trabajo en realidad de los parametros determinados o no determinados para la cuale existen los conocidos como 
    Rest Params, para que sirve eso? 
    pues no sirve para poder utilizar de una manera más eficiente la entrada distintas opciones como parametros que deberíamos usar.
    https://www.geeksforgeeks.org/args-kwargs-python/





● Parámetros por defecto
    Son los valores que definimos por default, esto sson declarados en los argumentos como valores default



● Docstring.
    Documentacion

● Funciones Lambda/Anónima
    Funciones Lambda
    https://www.freecodecamp.org/espanol/news/funciones-lambda-en-python-ejemplos-de-sintaxis/

    Un ejemplo similar a lo que vimos con closure en JS

    def multiplicar_por (n):
        return lambda x: x * n
  
    duplicar = multiplicar_por(2)
    triplicar = multiplicar_por(3)
    diez_veces = multiplicar_por(10)

    me permite retornar una funcion como parte de su valor de retorno, manteniendo su sintaxis inicial.

    Uso en una lista


Extra 
 
 Funciones usando funciones 
 Memoization
 DOC recomendaciones



Ejercicio 1 
Programar la función formatMiles() que reciba cómo argumento un número entero y
devuelva una cadena con el número y los separadores de miles y un punto y guión
al final. Por ejemplo, si recibe el número 12345678, debe devolver "12.345.678.-"

Ejercicio 2
Crear una función dado() que imite el lanzamiento de un dado, generando un
número al azar entre 1 y 6.


"""

# INICIO PROGRAMA

from aux_fun.funciones import imprimir_nombre
from aux_fun.funciones import imprimir_registros
from aux_fun.funciones import validar_pass
from aux_fun.funciones import contar_personas
from aux_fun.funciones import contar_personal
from aux_fun.funciones import suma
from aux_fun.funciones import mutabilidad
from aux_fun.funciones import sumar
from aux_fun.funciones import exponenciar
from aux_fun.funciones import generador


# resultado = generador(lambda a,b : a/b , 4,5)

# print(resultado)

# valor_retorno = mutabilidad({
#     'mascotas': True,
#     'dueño':'Yo mero'
# })


# print(valor_retorno)


# imprimir_nombre()

# valor_retorno = imprimir_registros(4)

# print(validar_pass('1232'))


# contar_personas('Rafa', 'Mariu')

# contar_personal('Rafa', 'Valeria', 'Martin','Daniel')


# resultado = suma(1,2,3,4,54,6,6)

# print(resultado)

# print( sum( [4,5,6,7,1,3,4,5]  ))



# *args

# def suma(a,b,*args):

#     return a+b+sum(args)


# print(suma(1,2,3,2,4,5,9))



# Uso practico de una funcion lambda

# https://www.analyticsvidhya.com/blog/2021/07/python-most-powerful-functions-map-filter-and-reduce-in-5-minutes/


# Tengo una lista de numeros :

# lista_nums = list(range(1,500,2*2))

# # solo numeros que sean divisibles por 3

# div_3  = filter( lambda n : n%3==0 , lista_nums)

# print( tuple(div_3) )


# def valor(a:str)->None:
#     """
#     Ejemplo de docstring.

#     -summary-
#     Recomendaciones de escritura de documentacion

#     @args:
#         a(str): ingresa valores para ser impreso en pantalla
    
#     returns None

#     """
#     print(a)
#     return None


# print(valor.__doc__)


# def clock_seg():
#     import time

#     for i in range(1, 21):
#         time.sleep(1)

#         print(f'\x1B[3m{i} seg\x1B[0m' , end = "\r")




# Memo es basicamente programacion dinámica,
# tiene como objeto aumentar la velocidad en la forma 
# que te regresan los datos

"""

import time

cache_memory={}


def exp_costosa(n):

    if n in cache_memory:
        print(f'{n} ya se encuentra en memoria>>')
        return cache_memory[n]

    print (f"Computing {n} ...")

    time.sleep(1)
    result= n**n

    cache_memory[n] = result

    return result



expect = exp_costosa(10)
print(f'El valor es : {expect}')

expect = exp_costosa(2)
print(f'El valor es : {expect}')

expect = exp_costosa(3)
print(f'El valor es : {expect}')

expect = exp_costosa(4)
print(f'El valor es : {expect}')

expect = exp_costosa(10)
print(f'El valor es : {expect}')

expect = exp_costosa(10)
print(f'El valor es : {expect}')


print(cache_memory)

"""

"""
Ejercicio 1 
Programar la función formatMiles() que reciba cómo argumento un número entero y
devuelva una cadena con el número y los separadores de miles y un punto y guión
al final. Por ejemplo, si recibe el número 12345678, debe devolver "12.345.678.-"
"""

# def format_miles(n:int)->str:
#     """
#     @arg
#         n(int) :  entero a dar formato
#     return 
#         resutl(str) : formato de entero
#     """
#     result 

#     return result


# n = 23

# data = str(n)[::-1]

# data_slice = []

# while len(data) >= 3:

#     result = data[:3][::-1]
#     data = data[3:]
#     data_slice.append(result)




# print(f"{data[::-1]}.{'.'.join(data_slice[::-1])}.-")