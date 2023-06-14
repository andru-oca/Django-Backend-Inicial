
# ABSTRACCION

class _Persona_:
    vive = True

    def muerto_vivo(self):
        if self.vive:
            print("aun esta vigente")
        else:
            print("esta fallecido")

    def soy(self):
        pass


class Premium:
    tiempo_vida_premium = "1 mes"

    def premium(self):
        print(f"El cliente tiene {self.tiempo_vida_premium} de plan premium")

# ENCAPSULACION 

class Cliente(_Persona_):
    status = True

    def __init__(self, nombre, cbu ,password):
        self.nombre = nombre
        self.__cbu = cbu
        self.__password = password

    # getters y setters
    def get_cbu(self):
        print(f"El cbu de la cliente{self.nombre} es:\n{self.__cbu}")

    def set_cbu(self,cbu):
        self.__cbu = cbu

    # setter
    def set_passwd(self,pwd):
        print(f"se ha cambiado el pass por: \n==> Old:{self.__password}")
        self.__password = pwd
        print(f"\n==> New: {self.__password}")

    def activo(self):
        if self.status:
            print(f"el cliente {self.__cbu} está activo")
        else:
            print(f"el cliente {self.__cbu} no está activo")
    

celeste = Cliente("celeste",172389471,"hola1234")

celeste.get_cbu() 
print(celeste._Cliente__cbu)

celeste.set_passwd("ola k ase?")


# HERENCIA


class ClienteFisico(Cliente):
    def __init__(self,nombre,cbu,password, dni):
        Cliente.__init__(self,nombre,cbu,password)
        self.dni = dni

    def soy(self):
        print("soy una cliente fisico")


class CuentasActivas:
    def __init__(self, cant_cuentas):
        self.cuentas_activas = cant_cuentas

    def mostra_cuentas_activas(self):
        print(f"la cantidad de cuentas activas es: {self.cuentas_activas}")

class ClienteJuridico(Cliente,Premium):
    def __init__(self, CUIT):
        self.CUIT = CUIT

    def soy(self):
        print("soy una cliente Juridico")

    def cuentas_activas(self,cuentas:CuentasActivas):
        cuentas.mostra_cuentas_activas()



cliente_fisico = ClienteFisico(
    "Ale",
    786781627381,
    "klkajskldjaklsjd",
    987128937
)

cliente_fisico.soy()

cliente_juridico= ClienteJuridico("29-79817238971-9")

cliente_juridico.set_cbu(871289378912)
cliente_juridico.activo()


print(f"ESTE CLIENTE ES JUIRIDICO, PERO => cual es su estatus de vida ?? -> {cliente_juridico.vive}")

cliente_juridico.premium()

cuentas_juridico = CuentasActivas(10)
cuentas_medium = CuentasActivas(5)


cliente_juridico.cuentas_activas(cuentas_medium)