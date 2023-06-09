


class Cliente:
    # atributo de clase
    activo = True

    #constructor
    # def __init__(self,numero_id,nombre,email,saldo):
    #     self.numero_id = numero_id
    #     self.nombre = nombre
    #     self.email = email
    #     self.saldo = saldo

    #constructor PRO
    def __init__(self, **kwargs):
        self.numero_id:int = kwargs["numero_id"]
        self.nombre:str = kwargs["nombre"]
        self.email:str = kwargs["email"]
        self.saldo:float = kwargs["saldo"]

    def presentacion(self):
        return f"""
            Soy el cliente #:{self.numero_id}
            Mi nombre es: {self.nombre}
            Tengo un saldo de: {self.saldo}
        """
    def cuenta_cliente(self):
        if self.saldo < 0 :
            return f"\tSaldo descubierto\n \t SALDO : ==> {self.saldo}"
        else:
            return f"\tSaldo a favor\n \t SALDO : ==> {self.saldo} "
    
    def cambiar_saldo(self, transaccion):
        self.saldo += transaccion
