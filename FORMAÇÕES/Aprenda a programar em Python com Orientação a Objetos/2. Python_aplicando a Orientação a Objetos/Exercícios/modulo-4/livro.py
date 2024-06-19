# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []

    def __init__(self, titulo: str, autor: str, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'"{self._titulo}" de {self._autor} - Publicado em {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
livro00 = Livro(titulo='Livro 1', autor='Um Autor', ano_publicacao='1999')
livro01 = Livro(titulo='Livro 2', autor='Outro Autor', ano_publicacao='2005')

print(livro00)
print(livro01)

# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
livro02 = Livro(titulo='Livro 3', autor='Mais um autor', ano_publicacao='1870')
livro02.emprestar()
print(livro02._disponivel)

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
print(Livro.verificar_disponibilidade(ano='2005'))

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
