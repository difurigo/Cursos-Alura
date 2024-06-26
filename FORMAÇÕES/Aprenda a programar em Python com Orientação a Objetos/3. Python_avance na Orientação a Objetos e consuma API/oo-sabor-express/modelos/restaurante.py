from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante():
    '''Representa um restaurante e suas características.'''

    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        '''
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma representação em string do restaurante.'''
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes.'''
        print('-' * 76)
        print(f'{'    Nome do restaurante'.ljust(26)} | {'      Categoria'.ljust(21)} | {' Avaliação'.ljust(11)} |  Status')
        print('-' * 76)

        for restaurante in cls.restaurantes:
            print(f'- {restaurante.nome.ljust(24)} | {restaurante.categoria.ljust(21)} | {'    ' + str(restaurante.media_avaliacoes).ljust(7)} |    {restaurante.ativo}')
        
        print('-' * 76)

    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante.'''
        return '✅' if self._ativo else '❎'
    
    @property
    def nome(self):
        '''Retorna o nome que foi atribuído ao restaurante'''
        return self._nome
    
    @property
    def categoria(self):
        '''Retorna a categoria que foi atribuída ao restaurante'''
        return self._categoria
    
    def alternar_status(self):
        '''Alterna o status de atividade do restaurante.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota: float):
        '''
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        '''
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante.'''
        if not self._avaliacao:
            return ' -'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round((soma_das_notas / quantidade_de_notas), 1)
        return media
    
    def adcionar_item_cardapio(self, item: ItemCardapio):
        '''Verifica se o item é um item do cardápio e adiciona o item à lista do cardápio'''
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'====== Cardápio do restaurante {self.nome} ======')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'tipo'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao} | Tamanho: {item.tamanho} | Tipo: {item.tipo}')
            elif hasattr(item, 'descricao'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}')
            elif hasattr(item, 'tamanho'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}')
