estoque = {
    "caderno": 10,
    "lapis": 25,
    "mochila": 87
}

print("estoque atualizado")

for chave, valor in estoque.items():

    print(f"produto - {chave} | qtd produto - {valor}")

    estoque.update({"mochila": 50, "caderno": 0})

    print("vendas efetuadas com sucesso!")

    print("estoque atualizado")

    for chave, valor in estoque.items():

        print(f"produto - {chave} | qtd produto - {valor}")