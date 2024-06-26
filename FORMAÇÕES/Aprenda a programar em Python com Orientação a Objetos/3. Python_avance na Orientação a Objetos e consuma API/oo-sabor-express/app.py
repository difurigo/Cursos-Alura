from modelos.restaurante import Restaurante
from modelos.cardapio import Bebida, Prato, Sobremesa
import os

restaurante_burguer_king = Restaurante(nome='Burguer King', categoria='Fast-Food')

# Bebidas do Buguer King
bebida_suco_melancia = Bebida(nome='Suco de Melancia', preco=8.50, tamanho=700)
bebida_suco_melancia.aplicar_desconto()
restaurante_burguer_king.adcionar_item_cardapio(bebida_suco_melancia)

# Pratos do Burguer King
prato_big_king = Prato(nome='Big King', preco=25.90, descricao='Pão, queijo, dois hamburgueres, salada e picles.')
prato_big_king.aplicar_desconto()
restaurante_burguer_king.adcionar_item_cardapio(prato_big_king)

# Sobremesas do Burguer King
sobremesa_casquinha = Sobremesa(nome='Casquinha', preco=3.50, descricao='Massa gelada do sabor escolhido', tipo='Sorvete', tamanho=200)
sobremesa_casquinha.aplicar_desconto()
restaurante_burguer_king.adcionar_item_cardapio(sobremesa_casquinha)

# restaurante_burguer_king.receber_avaliacao(cliente='Diego', nota=4)
# restaurante_burguer_king.receber_avaliacao(cliente='Vanessa', nota=3.6)

restaurante_badaroscas = Restaurante(nome='Badaroscas', categoria='Porção')
# restaurante_badaroscas.alternar_status()
# restaurante_badaroscas.receber_avaliacao(cliente='Nicolle', nota=3)
# restaurante_badaroscas.receber_avaliacao(cliente='Diego', nota=4.3)

restaurante_do_son = Restaurante(nome='Restaurante do Son', categoria='Self-Service')

def main():
    os.system('cls')
    restaurante_burguer_king.exibir_cardapio

if __name__ == '__main__':
    main()
