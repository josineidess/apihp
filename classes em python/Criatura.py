from Personagem import Personagem


class Criatura(Personagem):
    def __init__(self, nome, especie, foto, classificacao, descricao):
        super().__init__(nome, especie, foto)
        self.__classificacao = classificacao
        self.__descricao = descricao

    @property
    def classificacao(self):
        return self.__classificacao

    @property
    def descricao(self):
        return self.__descricao
