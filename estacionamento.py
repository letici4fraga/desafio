# estacionamento.py

class Estacionamento:
    def __init__(self):
        self.veiculos = {}

    def entrada_veiculo(self, veiculo):
        self.veiculos[veiculo.placa] = veiculo
        print("Veículo estacionado!")

    def saida_veiculo(self, placa, horas_estacionado):
        if placa in self.veiculos:
            veiculo = self.veiculos.pop(placa)
            valor_total = veiculo.calcular_valor(horas_estacionado)
            print(f"Valor total a pagar: R$ {valor_total:.2f}")
        else:
            print("Veículo não encontrado.")
