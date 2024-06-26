from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | {self.ligado}'
    
    @property
    def ligado(self):
        return 'Ligado' if self._ligado == True else 'Desligado'
    
    @abstractmethod
    def ligar(self):
        self._ligado = True
