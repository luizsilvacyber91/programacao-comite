def gerar_relatorio_vendas():

    dados = [
        {"produto": "Notebook", "quantidade": 15, "receita": 35000},

        {"produto": "Mouse", "quantidade": 50, "receita": 2500},

        {"produto": "Teclado", "quantidade": 30, "receita": 3000}
    ]
    return dados

def mostrar_relatorio_na_tela(relatorio):

    print("-" * 40)

    print("        RELATÓRIO DE VENDAS")

    print("-" * 40)

    print(f"{'Produto':<15} | {'Quantidade':<10} | {'Receita':<10}")

    print("-" * 40)

    for item in relatorio:

        print(f"{item['produto']:<15} | {item['quantidade']:<10} | R$ {item['receita']:<7.2f}")

    print("-" * 40)

relatorio = gerar_relatorio_vendas()

mostrar_relatorio_na_tela(relatorio)