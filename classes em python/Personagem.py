from abc import ABC, abstractmethod

class Personagem(ABC):
    @abstractmethod
    def __init__(self,nome,condicao,foto):
        self.__nome = nome
        self.__condicao = condicao
        self.__foto = foto

    @property
    def nome(self):
        return self.__nome

    @property
    def condicao(self):          
        return self.__condicao

    @property
    def foto(self):
        return self.__foto
