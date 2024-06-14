# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

print('\n1)')
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print('\n2)')
idade = int(input('Digite a sua idade: '))

if 0 < idade < 12:
    classificacao = 'criança'
elif 12 < idade < 18:
    classificacao = 'adolescente'
elif idade >= 18:
    classificacao = 'adulto'
else:
    print('Idade inválida.')

print(f'Você é {classificacao}')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

print('\n3)')
nome_usuario = 'DI_nossauro11'
senha_usuario = '123456'

usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite sua senha: ')

if nome_usuario == usuario and senha_usuario == senha:
    print('Login bem sucedido!') 
else:
    print('Usuário e/ou senha incorretos!')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

print('\n4)')
print('Digite as cordenadas:')
x = float(input('Cordenada x: '))
y = float(input('Cordenada y: '))

if x > 0 and y > 0:
    print(f'As cordenadas ({x}, {y}) pertencem ao Primeiro Quadrante do plano cartesiano.')
elif x < 0 and y > 0:
    print(f'As cordenadas ({x}, {y}) pertencem ao Segundo Quadrante do plano cartesiano.')
elif x < 0 and y < 0:
    print(f'As cordenadas ({x}, {y}) pertencem ao Terceiro Quadrante do plano cartesiano.')
elif x > 0 and y < 0:
    print(f'As cordenadas ({x}, {y}) pertencem ao Quarto Quadrante do plano cartesiano.')
else:
    print(f'As cordenadas ({x}, {y}) são um ponto que está sobre um eixou ou na origem.')
