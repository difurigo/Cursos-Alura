# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('1. Python na Escola de Programação da Alura.')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('\n2. Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos!\n')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
alura = 'ALURA'

for i in list(alura):
    print(f'{i}')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais
pi = 3.14159
pi_arredondado = round(pi, 2)

print(f'\nO valor arredondado de pi é: {pi_arredondado}.')