from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int, cor: str):
        super().__init__(marca, modelo)
        self._portas = portas
        self._cor = cor

    def __str__(self):
        return super().__str__() + f' | {self._portas} portas'
    
    def ligar(self):
        return super().ligar()
