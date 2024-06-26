from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str, tipo: str, tamanho: int):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    
    @property
    def tamanho(self):
        return f'{self._tamanho}ml'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)
