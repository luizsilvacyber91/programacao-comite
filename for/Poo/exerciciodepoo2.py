class ContaBancaria:

    def __init__(self, saldo_inicial=0):

        self.saldo = saldo_inicial

    def depositar(self, valor):

        if valor > 0:

            self.saldo += valor

            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        else:

            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):

        if valor <= 0:

            print("O valor do saque deve ser positivo.")

        elif valor <= self.saldo:

            self.saldo -= valor

            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        else:

            print("Saldo insuficiente para realizar o saque.")

    def ver_saldo(self):

        return f"Seu saldo atual é de R$ {self.saldo:.2f}"
    
minha_conta = ContaBancaria(3000)
print(minha_conta.ver_saldo()) 

minha_conta.depositar(1000) 
print(minha_conta.ver_saldo()) 

minha_conta.sacar(2000) 
print(minha_conta.ver_saldo()) 

minha_conta.sacar(15000) 
print(minha_conta.ver_saldo()) 

minha_conta.depositar(-500) 
