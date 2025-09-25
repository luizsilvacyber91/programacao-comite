palavra_secreta = input("informe a palavra secreta -> ")
palavra_encontrada = [","] * len(palavra_secreta)
chute_letra =''
tentativas = 10

for t in range(len(palavra_secreta)):
    chute_letras = input(f"chute uma letra(palavra_secreta)")

    for tentativa in range(len(palavra_secreta)):
        if palavra_secreta[t] == chute_letra:
            palavra_encontrada[t]

    if "-" not in palavra_encontrada:
        print("voce venceu!!!!")
        break

    print(f"Faltam apenas (tentativas - tentativa) tentativas")

else:
    print(f"voce perdeu, a palavra era (palavra_secreta)")
