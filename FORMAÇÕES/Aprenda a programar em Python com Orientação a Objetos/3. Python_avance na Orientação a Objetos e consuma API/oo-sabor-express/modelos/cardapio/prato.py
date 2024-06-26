from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        