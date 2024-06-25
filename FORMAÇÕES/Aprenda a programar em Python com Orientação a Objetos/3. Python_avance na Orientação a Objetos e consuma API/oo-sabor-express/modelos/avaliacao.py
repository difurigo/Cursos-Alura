class Avaliacao():
    '''
        Inicializa uma instância de Avaliação.

        Parâmetros:
        - cliente: O cliente que fez avaliação.
        - nota (float): A nota que o cliente deu ao restaurante.
        '''
    def __init__(self, cliente, nota: float):
        self._cliente = cliente
        self._nota = nota
        