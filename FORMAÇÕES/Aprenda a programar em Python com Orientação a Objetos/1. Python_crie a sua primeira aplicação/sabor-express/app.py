import os

restaurantes = [{'nome':'Restaurante do Son', 'categoria':'Self-Service', 'ativo':False},
                {'nome':'Outblack', 'categoria':'Australiana', 'ativo':True},
                {'nome':'Badaroscas', 'categoria':'Porções', 'ativo':False}]

def exibir_nome_programa():
    '''Essa função é responsável por exibir o nome do programa
    
    Output:
    - O nome do programa é impresso no console.
    '''

    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções que o programa pode realizar e que o usuário poderá escolher
    
    Outputs:
    - As opções são impressas no console.
    '''

    print('1. Cadastrar um novo restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado de um restaurante')
    print('4. Sair')

def opcao_invalida():
    '''Essa função é responsável por tratar o erro de uma escolha inválida feita pelo usuário dentre as opções existentes
    
    Outputs:
    - A mensagem de erro é impressa no console.
    '''

    print('\n⚠ Opção inválida. ⚠')
    voltar_para_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir um subtítulo
    
    Argumentos:
    - Recebe o texto que será utilizado como subtítulo como parâmetro
    
    Outputs:
    - O subtítulo é impresso no console.
    '''

    os.system('cls')
    print(texto)

def voltar_para_menu_principal():
    '''Essa função é responsável por voltar para o menu principal do programa
    
    Inputs:
    - Qualquer tecla
    
    Outputs:
    - Chama a função main()
    '''

    input('\nPrecione qualquer tecla para continuar')
    main()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adciona um novo restaurante à lista de restaurantes
    '''

    exibir_subtitulo('''
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ ▄▀█ █▀█   █░█ █▀▄▀█   █▄░█ █▀█ █░█ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▀█ █▀▄   █▄█ █░▀░█   █░▀█ █▄█ ▀▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
''')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria correspondente ao restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_para_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados
    
    Outputs:
    - Lista de restaurantes formatada em tabela é impressa no console
    '''

    exibir_subtitulo('''
    █░░ █ █▀ ▀█▀ ▄▀█ █▄░█ █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █ ▄█ ░█░ █▀█ █░▀█ █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█
''')

    print('-' * 60)
    print(f'{'  Nome do restaurante'.ljust(22)} | {'      Categoria'.ljust(21)} |   Estado')
    print('-' * 60)
    for restaurante in restaurantes:
        estado_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(21)} | {estado_restaurante}')

    print('-' * 60)
    voltar_para_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado de um restaurante
    
    Inputs:
    - Nome de um restaurante

    Outputs:
    - O novo estado do restaurante
    - Caso não seja encontrado, exibe a mensagem de não encontrado no console.
    '''

    exibir_subtitulo('''
    ▄▀█ █░░ ▀█▀ █▀▀ █▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀▀ █▀ ▀█▀ ▄▀█ █▀▄ █▀█   █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █▀█ █▄▄ ░█░ ██▄ █▀▄ █▀█ █░▀█ █▄▀ █▄█   ██▄ ▄█ ░█░ █▀█ █▄▀ █▄█   █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
''')
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
    '''Essa função é responsável por capturar a opção inserida pelo usuário e realizar a função escolhida
    
    Inputs:
    - Opção escolhida pelo usuário

    Outputs:
    - A função correspondente à escolha
    '''

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
    '''Essa função é responsável por exibir a mensagem de encerramento do programa
       
    Outputs:
    - Exibe uma mensagem de finalização no console
    '''

    exibir_subtitulo('Encerrando o app...\n')

def main():
    '''Essa função é responsável por iniciar o programa e exibir o menu principal
    
    Outputs:
    - Exibe o nome do programa no console
    - Exibe as opções para o usuário no console
    - Recebe a opção escolhida pelo usuário
    '''

    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
