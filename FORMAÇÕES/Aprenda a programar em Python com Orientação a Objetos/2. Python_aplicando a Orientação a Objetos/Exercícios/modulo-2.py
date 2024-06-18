# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

ford_ka = Carro(modelo='Ford Ka', cor='Branco', ano=2018)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante():
    def __init__(self, nome: str, categoria: str, telefone: str, cnpj: str, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.telefone = telefone
        self.cnpj = cnpj
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}' 

restaurante_burguer_king = Restaurante(nome='Burguer King', categoria='Fast-food', telefone='11999999999', cnpj='0134824972414-72847')

# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
print(restaurante_burguer_king)

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente():
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

cliente_00 = Cliente(nome='João', cpf='0284098414332', telefone='11999999999', email='joao@email.com')
cliente_01 = Cliente(nome='Carlos', cpf='r984509428553', telefone='11987654321', email='carlos@email.com')
cliente_02 = Cliente(nome='Janaina', cpf='798275375435905', telefone='11912345678', email='janaina@email.com')
