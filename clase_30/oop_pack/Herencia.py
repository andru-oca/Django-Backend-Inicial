import abc

from abc import abstractmethod
from abc import ABC

class PersonaAbstracta(ABC):

    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.email = kwargs.get("email","unknown")
        self.nacionalidad = kwargs.get("nacionalidad","unknown")
    
    @property
    @abstractmethod
    def dni(self):
        pass

    @dni.setter
    @abstractmethod
    def dni(self,dni):
        pass

    @property
    @abstractmethod
    def tramite(self):
        pass

    @tramite.setter
    @abstractmethod
    def tramite(self, tramite):
        pass





