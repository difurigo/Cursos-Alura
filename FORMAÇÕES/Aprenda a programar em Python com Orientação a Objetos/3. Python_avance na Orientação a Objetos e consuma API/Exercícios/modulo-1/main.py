from modelos.carro import Carro
from modelos.moto import Moto

# Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

# Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

# Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

# Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

# Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

# Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.

# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
moto_1 = Moto(marca='Yamaha', modelo='Cripton', tipo='casual')
moto_2 = Moto(marca='Honda', modelo='XRE', tipo='casual')
moto_3 = Moto(marca='BMW', modelo='S1000 RR', tipo='esportiva')

carro_1 = Carro(marca='Ford', modelo='Ford KA', portas=4, cor='Branco')
carro_2 = Carro(marca='Ssangyong', modelo='Actyon', portas=4, cor='Preto')
carro_2.ligar()
carro_3 = Carro(marca='Chevrolet', modelo='Celta', portas=2, cor='Cinza Chumbo')

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
print(moto_1)
print(moto_2)
print(moto_3)

print(carro_1)
print(carro_2)
print(carro_3)
