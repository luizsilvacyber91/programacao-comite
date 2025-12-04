class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, percentual_desconto):
        """
        Calcula o novo preço após aplicar um percentual de desconto.
        
        :param percentual_desconto: A porcentagem de desconto a ser aplicada (ex: 10 para 10%).
        :return: O novo preço com desconto.
        """
        if 0 <= percentual_desconto <= 100:
            valor_desconto = self.preco * (percentual_desconto / 100)
            novo_preco = self.preco - valor_desconto
            
            self.preco = round(novo_preco, 2) 
            return self.preco
        else:
            print("Erro: O percentual de desconto deve estar entre 0 e 100.")
            return self.preco
        
celular = Produto("Celular XYZ", 1500.00)

print(f"Preço original do {celular.nome}: R${celular.preco:.2f}")

desconto = 15
novo_preco = celular.aplicar_desconto(desconto)

print(f"Desconto aplicado: {desconto}%")
print(f"Novo preço do {celular.nome}: R${novo_preco:.2f}")

