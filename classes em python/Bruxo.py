from Personagem import Personagem

class Bruxo(Personagem):
    def __init__(self,nome,especie,foto,casa,varinha,sangue,nascimento,morte,figurinha,organizacoes,time,profissao,escola,patrono):
        super().__init__(nome,especie,foto)
        self.__casa = casa
        self.__varinha = varinha
        self.__sangue = sangue
        self.__nascimento = nascimento
        self.__morte = morte
        self.__figurinha= figurinha
        self.__organizacoes = organizacoes
        self.__time = time
        self.__profissao = profissao
        self.__escola = escola
        self.__patrono = patrono

    @property
    def casa(self):
        return self.__casa

    @property
    def varinha(self):
        return self.__varinha

    @property
    def sangue(self):
        return self.__sangue

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def morte(self):
        return self.__morte

    @property
    def figurinha(self):
        return self.__figurinha

    @property
    def organizacoes(self):
        return self.__organizacoes

    @property
    def time(self):
        return self.__time

    @property
    def profissao(self):
        return self.__profissao

    @property
    def escola(self):
        return self.__escola

    @property
    def patrono(self):
        return self.__patrono
