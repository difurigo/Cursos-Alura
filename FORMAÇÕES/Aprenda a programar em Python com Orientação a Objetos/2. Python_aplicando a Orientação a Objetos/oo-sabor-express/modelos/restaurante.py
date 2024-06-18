class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

    def listar_restaurantes():
        print('-' * 60)
        print(f'{'  Nome do restaurante'.ljust(22)} | {'      Categoria'.ljust(21)} |   Estado')
        print('-' * 60)

        for restaurante in Restaurante.restaurantes:
            estado_restaurante = 'Ativo' if restaurante.ativo == True else 'Inativo'
            print(f'- {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(21)} | {estado_restaurante}')
        
        print('-' * 60)

restaurante_praca = Restaurante('Praça', 'Italiana')
restaurante_burguer_king = Restaurante('Burguer King', 'Fast-food')

restaurantes = [restaurante_praca, restaurante_burguer_king]

Restaurante.listar_restaurantes()

# COLOCAR OBSERVAÇÃO NO FÓRUM SOBRE TIPAGEM DE VARIÁVEIS NAS CLASSES