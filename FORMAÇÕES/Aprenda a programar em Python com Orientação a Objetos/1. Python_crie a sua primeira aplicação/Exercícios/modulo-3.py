# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
lista_de_numeros = []
for i in range(1, 11):
    lista_de_numeros.append(i)

# Lista com quatro nomes;
lista_de_nomes = ['Diego', 'Vanessa', 'Melissa', 'Nicolle']

# Lista com o ano que você nasceu e o ano atual.
lista_de_anos = [2005, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for nome in lista_de_nomes:
    print(f'- {nome}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
for numero in lista_de_numeros:
    if numero % 2 != 0:
        print(numero)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número: '))
for i in range(1, 11):
    resultado = i * numero
    print(f'{i} x {numero} = {resultado}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
soma = 0

try:
    for numero in lista_de_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
def calcular_media_lista(lista):
    try:
        # Somar valores
        soma = 0
        for i in lista:
            soma += i

        # Dividir pela quantidade
        quantidade_algarismos = len(lista)
        media = soma / quantidade_algarismos
        
        return media
    except ZeroDivisionError:
        print('Não foi possível calcular a média: A lista está vazia.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
