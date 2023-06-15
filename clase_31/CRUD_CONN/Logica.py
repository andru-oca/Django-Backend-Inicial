from CRUD_CONN.User import User

class InsertUser:

    def insert_user(self, user:User):

        self.cnx.cursor()

        query = f"""
        INSERT INTO {self.db}.{self.table_name}
        (nombre,email,password) 
        VALUES
        {user.returned_string()};
        """
        self.cursor.execute(query)
        self.cnx.commit()

        print(f"Usuario {user.nombre} ha sido cargado en la base de datos")


class DeleteUser:

    def delete_user(self,email:str):

        self.cnx.cursor()

        try:
            query = f"""
            DELETE FROM {self.db}.{self.table_name}
            WHERE email = '{email}' ;
            """
            self.cursor.execute(query)
            self.cnx.commit()
            print(f"Usuario {email} ha sido eliminado de la base de datos")
        except Exception as e :
            print(e)

class ShowUsers:

    def show_users(self):
        self.cnx.cursor()

        try:
            query = f"""
            SELECT * FROM {self.db}.{self.table_name}
            ;
            """
            self.cursor.execute(query)
            usuarios = self.cursor.fetchall()

            print(f"USUARIOS CARGADOS EN LA BASE DE DATOS {self.db} TABLA: {self.table_name}")
            for user in usuarios:
                print(f"""
                        nombre : {user[1]}
                        email  : {user[2]}
                        -------------------------------------
                      """)
            
        except Exception as e :
            print(e)

class ShowUser:


    def show_user(self,email:str):
        self.cnx.cursor()

        try:
            query = f"""
            SELECT * FROM {self.db}.{self.table_name}
            WHERE email = '{email}'
            ;
            """
            self.cursor.execute(query)
            usuario = self.cursor.fetchall()
            
            if len(usuario) == 0:
                print(f"No hay usuario con el email : {email}")
                return False
            else:
                return True
        except Exception as e :
            print(e)

class UpdateUser:

    def update_user(self, email,data:str,valor_a_cambiar:str):

        if data == 'id' or data == 'email':
            print("Esos campos no están permitidos a realizar cambios")
            return

        try:
        
            self.cnx.cursor()

            query = f"""
            UPDATE {self.db}.{self.table_name}
            SET {data} = '{valor_a_cambiar}'
            WHERE email = '{email}'
            """
            self.cursor.execute(query)
            self.cnx.commit()

            if data == "password":
                print(f"Usuario {email} ha cambiado su {data} por {valor_a_cambiar}")

            else:
                print(f"Usuario {email} ha cambiado su {data} por {valor_a_cambiar}")
            
        except Exception as e:
            print(e)

