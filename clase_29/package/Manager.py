from package.Cliente import Cliente

class Manager:
    db_cliente = []
    db_clientes_borrados = []

    def __init__(self, **kwargs):
        self.path = kwargs.get("path","")
        self.nombre_empresa =  kwargs.get("nombre_empresa","empresa_default")

    def __str__(self):
        return f"MANAGER DE CLIENTES: {self.nombre_empresa}"

    def create_cliente(self , cliente:Cliente):
        self.db_cliente.append(cliente)
        print(
            f"""
            Bienvenido!
            El cliente : {cliente.nombre} ha sido agregado.
            """
        )

    def read_clientes(self):
        for cliente in self.db_cliente:
            print(cliente.presentacion())
            print(cliente.cuenta_cliente())


    def update_cliente_saldo(self, **kwargs):
        nombre = kwargs["nombre_cliente"]
        valor_transaccion = kwargs["valor_transaccion"]

        for index,cliente  in enumerate(self.db_cliente):
            if cliente.nombre == nombre:
                cliente.cambiar_saldo(valor_transaccion)
        
            
    def delete_cliente(self, email_cliente):
        
        self.db_clientes_borrados.append(*[

           cliente for cliente in self.db_cliente if cliente.email == email_cliente

        ])

        self.db_cliente =  [

           cliente for cliente in self.db_cliente if cliente.email != email_cliente

        ]

        print(
        f"""
            El cliente con el email: {email_cliente}
            a sido dado de baja
        """)

        # for index,cliente  in enumerate(self.db_cliente):
        #     if cliente.email == email_cliente:
        #         print(f"""
        #             El cliente : {cliente.nombre}
        #             a sido dado de baja
        #         """)
        #         self.db_cliente.pop(index)
        
