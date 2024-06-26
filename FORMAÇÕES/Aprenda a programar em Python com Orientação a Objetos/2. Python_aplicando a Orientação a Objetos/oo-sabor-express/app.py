from modelos.restaurante import Restaurante
import os

restaurante_burguer_king = Restaurante(nome='Burguer King', categoria='Fast-Food')
restaurante_burguer_king.receber_avaliacao(cliente='Diego', nota=4)
restaurante_burguer_king.receber_avaliacao(cliente='Vanessa', nota=3.6)

restaurante_badaroscas = Restaurante(nome='Badaroscas', categoria='Porção')
restaurante_badaroscas.alternar_status()
restaurante_badaroscas.receber_avaliacao(cliente='Nicolle', nota=3)
restaurante_badaroscas.receber_avaliacao(cliente='Diego', nota=4.3)

restaurante_do_son = Restaurante(nome='Restaurante do Son', categoria='Self-Service')

def main():
    os.system('cls')
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
