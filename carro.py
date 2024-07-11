# carro.py

from veiculo import Veiculo

class Carro(Veiculo):
    valor_por_hora = 10.0

    def calcular_valor(self, horas_estacionado):
        return horas_estacionado * self.valor_por_hora
