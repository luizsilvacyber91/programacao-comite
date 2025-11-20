def encontrar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo) as arquivo:
            texto = arquivo.readlines()
            cont = 0
            for linha in texto:
                if palavra.lower() in linha.lower():
                    cont += 1
                    print(
                        f'palavra"(palavra.lower())" '
                        f'encontrada! '
                        f'qtd palavra encontradas (cont)')
    except FileNotFoundError:
        print('Arquivo Não Encontrado!!!')

def main():
    nome_arquivo = 'novo_texto.txt'
    palavra = iNPUT('Qual a palavra esta procurando? -> ')
    encontrar_palavra(nome_arquivo, palavra)

    main()
                    