from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import os

restaurante_burguer_king = Restaurante(nome='Burguer King', categoria='Fast-Food')
bebida_suco_melancia = Bebida(nome='Suco de Melancia', preco=8.50, tamanho=700)
prato_big_king = Prato(nome='Big King', preco=25.90, descricao='Pão, queijo, dois hamburgueres, salada e picles.')

# restaurante_burguer_king.receber_avaliacao(cliente='Diego', nota=4)
# restaurante_burguer_king.receber_avaliacao(cliente='Vanessa', nota=3.6)

restaurante_badaroscas = Restaurante(nome='Badaroscas', categoria='Porção')
# restaurante_badaroscas.alternar_status()
# restaurante_badaroscas.receber_avaliacao(cliente='Nicolle', nota=3)
# restaurante_badaroscas.receber_avaliacao(cliente='Diego', nota=4.3)

restaurante_do_son = Restaurante(nome='Restaurante do Son', categoria='Self-Service')

def main():
    os.system('cls')
    print(bebida_suco_melancia)
    print(prato_big_king)

if __name__ == '__main__':
    main()
