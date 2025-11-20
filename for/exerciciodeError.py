while True:
    
    try:

        numero = int(input("Por favor, digite um número inteiro: "))
        
        break

    except ValueError:
        
        print("Entrada inválida! Por favor, digite um número inteiro válido.")

print(f"O número digitado foi: {numero}")