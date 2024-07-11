# main.py

from estacionamento import Estacionamento
from carro import Carro
from moto import Moto

def main():
    estacionamento = Estacionamento()

    while True:
        print("\nMenu:")
        print("1. Entrada de veículo")
        print("2. Saída de veículo")
        print("3. Encerramento do programa")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            placa = input("Placa do veículo: ")
            modelo = input("Modelo do veículo: ")
            marca = input("Marca do veículo: ")
            tipo = input("Tipo de veículo (carro/moto): ")

            if tipo == 'carro':
                veiculo = Carro(placa, modelo, marca)
            elif tipo == 'moto':
                veiculo = Moto(placa, modelo, marca)
            else:
                print("Tipo de veículo inválido.")
                continue

            estacionamento.entrada_veiculo(veiculo)

        elif opcao == '2':
            placa = input("Placa do veículo: ")
            horas_estacionado = int(input("Quantidade de horas estacionado: "))
            estacionamento.saida_veiculo(placa, horas_estacionado)

        elif opcao == '3':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
