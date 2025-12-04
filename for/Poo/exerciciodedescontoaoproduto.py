def calcular_preco_com_desconto(preco_original, percentual_desconto):

    if not (0 <= percentual_desconto <= 100):

        return "Erro: Percentual inválido"

    valor_desconto = preco_original * (percentual_desconto / 100)

    preco_final = preco_original - valor_desconto
    
    return round(preco_final, 2)

preco_tenis = 300.00

desconto_tenis = 20

preco_final = calcular_preco_com_desconto(preco_tenis, desconto_tenis)

print(f"O preço final do tênis com {desconto_tenis}% de desconto é R${preco_final:.2f}")