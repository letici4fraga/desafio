# veiculo.py

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, modelo, marca):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca

    @abstractmethod
    def calcular_valor(self, horas_estacionado):
        pass
