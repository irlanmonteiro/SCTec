class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
    
    def mostrar(self):
        print(f'A placa deste veículo é {self.placa}')

veiculo1 = Carro('Onix','RXQ5E79','2023')   
veiculo2 = Carro('Tracker','TTA7253','2025')   
veiculo3 = Carro('Equinox','SZU3I12','2024')

veiculo2.mostrar()