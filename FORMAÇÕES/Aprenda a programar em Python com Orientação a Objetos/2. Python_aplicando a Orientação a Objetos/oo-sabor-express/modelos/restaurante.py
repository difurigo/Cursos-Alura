from modelos.avaliacao import Avaliacao

class Restaurante():
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = [] 
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print('-' * 76)
        print(f'{'    Nome do restaurante'.ljust(26)} | {'      Categoria'.ljust(21)} | {' Avaliação'.ljust(11)} |  Status')
        print('-' * 76)

        for restaurante in cls.restaurantes:
            print(f'- {restaurante.nome.ljust(24)} | {restaurante.categoria.ljust(21)} | {'    ' + str(restaurante.media_avaliacoes).ljust(7)} |    {restaurante.ativo}')
        
        print('-' * 76)

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota: float):
        avaliacao = Avaliacao(cliente=cliente, nota=nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round((soma_das_notas / quantidade_de_notas), 1)
        return media
