from oop_pack.Herencia import PersonaAbstracta


class TramitesDni(PersonaAbstracta):
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self,dni):
        self._dni = dni

    @property
    def tramite(self):
        return self._tramite 

    @tramite.setter
    def tramite(self, tramite):
        self._tramite = tramite



class Italiano(TramitesDni):
    __ita_prefix = "italian"

    def get_prefix(self):
        return self.__ita_prefix

    def printDNI(self):
        return f"{self.__ita_prefix}\t-->\t{self.dni}"

class Argentino(TramitesDni):
    RENAPER = "ARG"
    def printDNI(self):
        return f"{self.RENAPER}-{self.dni}"

class Peruano(TramitesDni):
    PER = "pe"

    def printDNI(self):
        return f"{self.dni}-{self.PER}"

class Brasilero(TramitesDni):
    def printDNI(self):
        return f"Tutto BOM - Legal"