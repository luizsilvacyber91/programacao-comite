
numero_aleatorio = 9
adivinhacao = 0 

while True:
    
    try:
        adivinhacao_str = input("Tente adivinhar o número (entre 1 e 10): ")
        adivinhacao = int(adivinhacao_str) 

    except ValueError:
        print("Por favor, insira um número válido.")
        
    if adivinhacao == numero_aleatorio:
        print("Parabéns! Você acertou!")

        break 

    elif adivinhacao < numero_aleatorio:
        print("Tente um número maior!")

    else:
        print("Tente um número menor!")

         