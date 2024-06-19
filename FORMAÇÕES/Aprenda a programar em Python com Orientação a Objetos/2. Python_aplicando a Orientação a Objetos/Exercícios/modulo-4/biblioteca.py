from livro import Livro

livro_biblioteca = Livro(titulo='Livro da Biblioteca', autor='Um autor', ano_publicacao='2018')
livro_biblioteca.emprestar()
print(livro_biblioteca._disponivel)

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")
