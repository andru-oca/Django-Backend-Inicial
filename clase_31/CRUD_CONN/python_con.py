"""
NECESITO INSTALAR PAQUETES TALES COMO 

    - pip install pymysql
    - https://pypi.org/project/pymysql/

"""

import pymysql
import os


from CRUD_CONN.data_protegida import    MYSQLDATABASE,\
                                        MYSQLHOST,\
                                        MYSQLPASSWORD,\
                                        MYSQLPORT,\
                                        MYSQLUSER,\
                                        MYSQL_TABLE


from CRUD_CONN.Logica import InsertUser,DeleteUser,ShowUsers,UpdateUser,ShowUser


class CrudApp(InsertUser,DeleteUser,ShowUsers,UpdateUser,ShowUser):

    table_name =  MYSQL_TABLE
    

    def __init__(self,**kwargs):

        
        self.db = kwargs["db"]
        
        try:
            self.cnx = pymysql.connect(
                
                user = kwargs["user"],
                host = kwargs["host"],
                password =kwargs["password"]
            )

            
            print("Conexion establecida")
            self.cursor = self.cnx.cursor()

            # creando la tabla y la base de datos

            print("Se genera la base de datos y la tabla")

            db_create = f"""
            CREATE DATABASE IF NOT EXISTS {self.db};
            """

            self.cursor.execute(db_create)
            self.cnx.commit()

            query = f"""
            CREATE TABLE IF NOT EXISTS {self.db}.{self.table_name}(
                            user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL
                            
            );
            """
            self.cursor.execute(query)
            self.cnx.commit()

        except Exception as Error:
            print(Error)



crud = CrudApp(
                host = MYSQLHOST,
                password = MYSQLPASSWORD,
                port = MYSQLPORT,
                user = MYSQLUSER,
                db = MYSQLDATABASE
)