from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + f' | Tipo {self._tipo}'
    
    def ligar(self):
        return super().ligar()
