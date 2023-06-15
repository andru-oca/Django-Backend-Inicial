from CRUD_CONN.python_con import crud
from CRUD_CONN.data_protegida import  MYSQL_TABLE
from CRUD_CONN.User import User

def main():

    print("software para crear CRUD de USUARIOS")

    while True:
        print("""
        elija una opcion para continuar
        1 -> crear usuario
        2 -> borrar usuario
        3 -> actualizar usuario
        4 -> mostrar usuarios
        0 --> para salir
        """)

        opcion = input("")

        if opcion == "0":
            print("Gracias por usar el software")
            break
    
        if opcion not in ["1","2","3","4"]:
            print("opcion no es válida\nVuelva a intentarlo")

            
        if opcion == "1":
            print("Vamos a crear al usuario")
            nombre =input("Ingresar nombre:\n")
            email = input("Ingresar email:\n")
            password = input("Ingresar password:\n")

            user = User(
                nombre = nombre , 
                email = email ,
                password = password
                )
            
            crud.insert_user(user)

        if opcion == "2" :
            print("vamos a borrar un usuario")
            email = input("Ingresar email:\n")

            if not crud.show_user(email):
                continue

            crud.delete_user(email)
        
        if opcion == "3":
            print("vamos a actualizar un usuario")
            email = input("Ingresar email:\n")

            print("Verifiquemos si el usuario existe")
            if not crud.show_user(email):
                continue
            print("Existe! vamos a actualizar sus datos")
            data_cambiar = input("campo a cambiar:\n")
            nuevo_valor = input("nuevo valor:\n")

            crud.update_user(email,data_cambiar,nuevo_valor)

        if opcion == "4" :
            print("Veamos todos los usuarios")
            crud.show_users()


if __name__ == "__main__":
    main()
