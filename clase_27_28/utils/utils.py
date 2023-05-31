def imprimir_nombre():
    
    print('Hola mundo')

    return None


def imprimir_registros( numero:int )->str:
    """
    ESTO ME IMPRIME UNA LISTA ORDENADA DE REGISTROS
    """
    import time

    for n in range(numero):

        print(n , end="\r")

        time.sleep(0.5)

    return 'ola k ase?'


def validar_pass(pwd:str)->bool:

    # valor_booleano = None

    # if pwd == '1234':
    #     valor_booleano = True
    # else:
    #     valor_booleano = False

    # return valor_booleano

    return pwd == '1234'





# funcion que me permite hacer un conteo de personal


def contar_personas(orador, persona, persona2 ='claudio' ):

    print(orador)
    print(persona)
    print(persona2)

    return None


def contar_personal(orador, *personas):

    print(orador)

    for persona in personas:
        print(persona)
    
    return None



def suma(a,b,*args):

    return a+b+sum(args)



def mutabilidad(persona:dict)->dict:
    """
    -summary-
    
    Mutar el valor del argumento

    @args:
        persona(dict): ingesta a la funcion un valor
    
    returns:
        dict_retorno(dict): dict mutado

    """

    persona['patos'] = ['donald','trump','🎸','lucas']

    dict_retorno = persona

    return dict_retorno


# Callback

def sumar( n, m):
    return n+m


def exponenciar(n,m):
    return n**m


def generador(cb,a ,b):

    return cb(a,b)
