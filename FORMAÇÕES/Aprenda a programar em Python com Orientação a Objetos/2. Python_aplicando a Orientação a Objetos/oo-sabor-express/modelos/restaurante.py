class Restaurante():
    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print('-' * 63)
        print(f'{'    Nome do restaurante'.ljust(26)} | {'      Categoria'.ljust(21)} |  Status')
        print('-' * 63)

        for restaurante in cls.restaurantes:
            print(f'- {restaurante.nome.ljust(24)} | {restaurante.categoria.ljust(21)} |    {restaurante.ativo}')
        
        print('-' * 63)

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

restaurante_praca = Restaurante(nome='Praça', categoria='Italiana')
restaurante_praca.alternar_status()

restaurante_burguer_king = Restaurante(nome='Burguer King', categoria='Fast-food')

restaurantes = [restaurante_praca, restaurante_burguer_king]

print(restaurante_burguer_king)
Restaurante.listar_restaurantes()

# COLOCAR OBSERVAÇÃO NO FÓRUM SOBRE TIPAGEM DE VARIÁVEIS NAS CLASSES