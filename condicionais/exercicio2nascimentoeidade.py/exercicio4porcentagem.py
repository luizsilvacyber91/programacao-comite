def calcular_aumento(valor, porcentagem):
    
    valor_aumento = valor * (porcentagem / 100)

    return valor_aumento

valor_original = 500.00

percentual_aumento = 10.0

aumento = calcular_aumento(valor_original, percentual_aumento)

print(f"Valor original: R$ {valor_original:.2f}")

print(f"Porcentagem de aumento: {percentual_aumento}%")

print(f"Valor do aumento: R$ {aumento:.2f}")

print(f"Novo valor total: R$ {valor_original + aumento:.2f}")