class Carro:

    def __init__(self, modelo, ano):
        
        self.modelo = modelo

        self.ano = ano

    def ligar(self):

        print(f'Ligando o {self.modelo} . {self.ano}')

def main():

    carro1 = Carro(input('Modelo do carro -> '),
                        input('Ano do carro -> '))
        
    carro2 = Carro(input('Modelo do carro -> '),
                       input('Ano do carro -> '))
        
    carro1.ligar()
    carro2.ligar()

main()