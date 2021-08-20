from abc import ABC, abstractmethod

class Personagem(ABC):
    @abstractmethod
    def __init__(self,nome,especie,foto):
        self.__nome = nome
        self.__especie = especie
        self.__foto = foto

    @property
    def nome(self):
        return self.__nome

    @property
    def especie(self):          
        return self.__especie

    @property
    def foto(self):
        return self.__foto
