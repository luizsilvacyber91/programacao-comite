while True:
    entrada = input("Digite algo (ou 'sair' para terminar): ")
    if entrada.lower() == "sair":  
        break  
    else:
        print(f"Você digitou: {entrada}")

print("Programa encerrado.")