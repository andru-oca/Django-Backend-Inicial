'''
CRUD ==> 
    CREATE
    RETRIEVE   <=> GET verb HTTP
    UPDATE
    DELETE
'''


##  CRUD => CLIENTES 
#               MOSTRAR DEUDAS
#               CLIENTE ID
#               SALUDO

#   PROGRAMA: CRUD --> DE CLIENTES
#   MUESTRE LOS CLIENTE CON SUS RESPECTIVAS DEUDAS


from package.Cliente import Cliente
from package.Manager import Manager


cliente_dalila  = Cliente(
    nombre = "dalila",
    saldo   = 100,
    numero_id = 9898 ,
    email = "dalila@mail.com"
)

cliente_maximiliano = Cliente(
    nombre = "maximiliano",
    saldo   = -10,
    numero_id = 9991 ,
    email = "maxi@mail.com"
)


manager_clientes = Manager(
    nombre_empresa = "Kentucky"
)

# print(
#     cliente_dalila.cuenta_cliente(),
# )

print("CREATE","*"*50)

manager_clientes.create_cliente(cliente_dalila)
manager_clientes.create_cliente(cliente_maximiliano)


print("READ","*"*50)
manager_clientes.read_clientes()


print("UPDATE","*"*50)

manager_clientes.update_cliente_saldo(
    nombre_cliente = "maximiliano",
    valor_transaccion = 500
)

manager_clientes.read_clientes()

print("DELETE","*"*50)

manager_clientes.delete_cliente("dalila@mail.com")
manager_clientes.read_clientes()
print(manager_clientes.db_clientes_borrados)






