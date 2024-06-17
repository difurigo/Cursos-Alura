import os

restaurantes = [{'nome':'Restaurante do Son', 'categoria':'Self-Service', 'ativo':False},
                {'nome':'Outblack', 'categoria':'Australiana', 'ativo':True},
                {'nome':'Badaroscas', 'categoria':'Porções', 'ativo':False}]

def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar um novo restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado de um restaurante')
    print('4. Sair')

def opcao_invalida():
    print('\n⚠ Opção inválida. ⚠')
    voltar_para_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def voltar_para_menu_principal():
    input('\nPrecione qualquer tecla para continuar')
    main()

def cadastrar_restaurante():
    exibir_subtitulo("""
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ ▄▀█ █▀█   █░█ █▀▄▀█   █▄░█ █▀█ █░█ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▀█ █▀▄   █▄█ █░▀░█   █░▀█ █▄█ ▀▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
""")

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria correspondente ao restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_para_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("""
    █░░ █ █▀ ▀█▀ ▄▀█ █▄░█ █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █ ▄█ ░█░ █▀█ █░▀█ █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█
    """)

    print('-' * 60)
    print(f'{'  Nome do restaurante'.ljust(22)} | {'      Categoria'.ljust(21)} |   Estado')
    print('-' * 60)
    for restaurante in restaurantes:
        estado_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(21)} | {estado_restaurante}')

    print('-' * 60)
    voltar_para_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("""
▄▀█ █░░ ▀█▀ █▀▀ █▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀▀ █▀ ▀█▀ ▄▀█ █▀▄ █▀█   █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
█▀█ █▄▄ ░█░ ██▄ █▀▄ █▀█ █░▀█ █▄▀ █▄█   ██▄ ▄█ ░█░ █▀█ █▄▀ █▄█   █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
""")
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')

    voltar_para_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo('Encerrando o app...\n')

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
