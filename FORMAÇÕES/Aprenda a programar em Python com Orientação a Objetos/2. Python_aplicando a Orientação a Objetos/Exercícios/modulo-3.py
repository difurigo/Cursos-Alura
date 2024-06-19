# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str = ''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self._nome}, {self._idade} anos - {self._profissao}'
    
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}!'

    def aniversario(self):
        self._idade += 1

pessoa01 = Pessoa(nome='Rodrigo', idade=25)
pessoa01 = Pessoa(nome='Diego', idade=18, profissao='Desenvolvedor')
print(pessoa01.saudacao)
pessoa01.aniversario()
print(pessoa01)

# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular: str, saldo: float, ativo: bool = False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
    
    def __str__(self):
        return f'Titular: {self._titular} - Saldo: R${self._saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
conta01 = ContaBancaria(titular='Vanessinha', saldo=100.0)
conta02 = ContaBancaria(titular='Carlinhos', saldo=280.50)

print(conta01)
print(conta02)

# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
ContaBancaria.ativar_conta(conta01)
print(conta01.ativo)

# Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
# Crie uma instância da classe e imprima o valor da propriedade titular.
print(f"Titular da conta 1: {conta01.titular}")

# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome: str, idade: int, endereco: str, cpf: str, profissao: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    
    @classmethod
    def criar_conta(cls, titular: str, saldo_inicial: float):
        conta = ContaBancaria(titular=titular, saldo=saldo_inicial)
        return conta
    
cliente00 = ClienteBanco(nome='Diego', idade=18, endereco='Rua das Palmeiras', cpf='123.456.789-01', profissao='Desenvolvedor')
cliente01 = ClienteBanco(nome='Vanessa', idade=48, endereco='Rua das Flores', cpf='987.654.321-01', profissao='Gerente de Relacionamento de TI')
cliente02 = ClienteBanco(nome='Alan', idade=40, endereco='Rua Sem Nome', cpf='111.222.333-44', profissao='Mecânico')

# Crie um método de classe para a conta ClienteBanco.
conta_cliente00 = ClienteBanco.criar_conta('Diego', 200)
print(f"Conta de {conta_cliente00.titular} criada com saldo inicial de R${conta_cliente00.saldo}")
