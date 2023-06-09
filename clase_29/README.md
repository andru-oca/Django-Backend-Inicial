LOS OBJETOS EN PYTHON
---
- [COMO FUNCIONA UN OBJETO ](https://www.digitalocean.com/community/tutorials/python-classes-objects
)

Clases y objetos: 

Que son las clases ? son blueprints o plantillas de creación de objetos



```

class <nombre_clase>:
    atributos de clase
    .
    .
    atributos de clases
    
    <constructor_de_clase>
    .
    .
    .

    <metodos>
    .
    .
    .


EJEMPLO:

class Persona:
    '''
    atributos
        
    '''

    nombre = 'Martin'
    edad = 34
    email = 'data@mail.com'
    dni  = 93_940_099


    '''
    metodos
    '''

    def saludo(self, persona:str)->None: #metodo no estático
        print(f'Hola!! {persona}')

    @staticmethod
    def saludo_static(persona:str)->None: #metodo estático
        print(f'Hola!! {persona}')
    

```


- [ENCAPSULAMIENTO y OTRAS VERDURAS](https://ellibrodepython.com/encapsulamiento-poo)


[HERENCIA SIMPLE ](https://pythones.net/herencia-simple-y-multiple-python-oop/#:~:text=La%20herencia%20simple%20tiene%20lugar,atributos%20de%20la%20clase%20padre.)
[HERENCIA SIMPLE PART 2](https://ellibrodepython.com/herencia-en-python)

* RELACIONES : [RELACIONES TIPO ](https://www.w3resource.com/java-tutorial/inheritance-composition-relationship.php)
    - IS-A -> HERENCIA DE CLASE
    - HAS-A -> RELACION DE COMPOSICION


- EJERCICIO GENERAL MANAGER DE CERVEZAS
    - MANAGER :  VA A PERMITIR GENERAR CRUD DE ELEMENTOS.
    - PERSISTENCIA : PRIMERA INSTANCIA : FILESYSTEM
    - PERSISTENCIA DB : CONNECT CON MYSQL