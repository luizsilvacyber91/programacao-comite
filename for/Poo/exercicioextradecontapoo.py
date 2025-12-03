class Conta:
    def __init__(self, saldo):
        self.saldo = int(saldo)

    def depositar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} |')
        self.saldo += valor
        print(f'Saldo atual | {self.saldo} |')

    def sacar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} |')
        self.saldo -= valor
        print(f'Saldo atual | {self.saldo} |')

def main():
    minha_conta = Conta(3000)
    minha_conta.sacar(int(input('informe valor do saque -> ')))

    print(f'\no saldo atual é {minha_conta.saldo}\n')

    minha_conta.depositar(int(input('informe valor do deposito -> ')))

main()