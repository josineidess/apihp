class Feitico:
    def __init__(self,nome,efeito,cor,sequencia_de_movimentos,dificuldade):
        self.__nome = nome
        self.__efeito = efeito
        self.__sequencia = sequencia_de_movimentos
        self.__dificuldade = dificuldade


    @property
    def nome(self):
        return self.__nome

    @property
    def efeito(self):
        return self.__efeito

    @property
    def sequencia(self):
        return self.__sequencia

    @property
    def dificuldade(self):
        return self.__dificuldade
