# moto.py

from veiculo import Veiculo

class Moto(Veiculo):
    valor_por_hora = 5.0

    def calcular_valor(self, horas_estacionado):
        return horas_estacionado * self.valor_por_hora
