estoque = {
    "caderno": 10,
    "lapis": 25,
    "mochila": 87
}

print("adicionando um novo item ao estoque")

estoque["corretivo"] = 45

print("estoque atualizado")

for chave, valor in estoque.items():

    print(f"produto - {chave} | adicionar  {valor}")

print("removendo um produto do estoque")

del estoque["lapis"]

print("estoque atualizado")

for chave, valor in estoque.items():

    print(f"produto - {chave} | qtd produto - {valor}")

print("limpando o estoque")

estoque.clear()

print(f"estoque limpo - {estoque}")