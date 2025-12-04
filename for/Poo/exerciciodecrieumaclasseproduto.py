class Produto:
    
    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def __str__(self):

        return f"{self.nome}: R${self.preco:.2f}"

produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 89.90)

print(f"Nome do produto 1: {produto1.nome}")
print(f"Preço do produto 2: R${produto2.preco:.2f}")

print(produto1)
print(produto2)