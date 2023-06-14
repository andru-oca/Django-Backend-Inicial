
# _HERENCIA


class _Persona_:
    piernas:bool = True

    def saludo():
        pass

class Padre(_Persona_):
    def __init__(self, nombre , color_ojos):
        self.nombre = nombre
        self.color_ojos = color_ojos


    def saludo(self):
        return "Hola!! como vas?"


class Madre:
    ganas_de_formar_familia = True

    def __init__(self,baila:bool):
        self.baila =baila

    def cocinar_rico(self):
        return "se cocinar excelente un pastel de papas!"

class HijoMenor(Padre,Madre):

    def __init__(self,nombre , color_ojos,altura,baila=False):
        Padre.__init__(self, nombre , color_ojos)
        Madre.__init__(self, baila)
        self.altura = altura

    def saludo(self):
        return "YO SALUDO GRITANDO!!!"


class Hijo(Padre,Madre):
    __cuenta_bancaria:str

    def __init__(self,nombre , color_ojos,altura,baila=False):
        Padre.__init__(self, nombre , color_ojos)
        Madre.__init__(self, baila)
        self.altura = altura

    
    def rebelde(self):
        return "me gusta rbd"

    # setear datos a los privados
    def agrear_cuenta(self, cuenta_bancaria):
        self.__cuenta_bancaria = cuenta_bancaria
    # get datos a los privados
    def mostrar_cuenta_bancaria(self):
        return self.__cuenta_bancaria

    


class Hija(Padre):
    def __init__(self, nombre , color_ojos , coqueta):
        Padre.__init__(self, nombre , color_ojos)
        
        self.coqueta =  coqueta


    def reparar(self):
        return "puedo reparar todo"

    def carpinteria(self):
        return "te armo un banquito"
        

martin = Hijo("martin","azules" , 1.75)
benja= HijoMenor("benjamin","marron", 2.0,True)

cecilia = Hija("cecilia","gris",100)

print("soy martin")
print(martin.rebelde())
print(martin.saludo())

print("#"*50)
print(martin.cocinar_rico())
print(martin.ganas_de_formar_familia)
print(martin.baila)

print("#"*50)
print("soy cecilia")
print( cecilia.reparar())
print( cecilia.carpinteria())
print( cecilia.saludo())


print("#"*50)
martin.agrear_cuenta(1123123123)
# print(martin.mostrar_cuenta_bancaria())
print(martin._Hijo__cuenta_bancaria)

print("#"*50)
print(benja.saludo())

print(martin.piernas)




# decorador


def deco_zero(fn):
    def analisis(a,b):
        if b==0:
            print("zapallo, como vas a divir por cero??")
            return
        return fn(a,b)
    
    return  analisis


@deco_zero
def division(a,b):
    print(a/b)



division(1,10)

