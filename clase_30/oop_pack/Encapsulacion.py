class Persona:
    __dni = None
    __tramite = None

    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.email = kwargs.get("email","unknown")
        self.nacionalidad = kwargs.get("nacionalidad","unknown")


    def __str__(self):
        return f"""
        Nombre:     {self.nombre}
        Email:      {self.email}
        Nac.:       {self.nacionalidad}
        dni :       {self.get_dni()}
        tramite:    {self.get_tramite()}
        """

    def set_dni(self,dni):
        self.__dni = dni

    def get_dni(self):
        return self.__dni

    def set_tramite(self,tramite):
        self.__tramite = tramite

    def get_tramite(self):
        return self.__tramite