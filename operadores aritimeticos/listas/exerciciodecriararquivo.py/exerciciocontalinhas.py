def contar_linhas():
    try:

       with open('log.txt') as arquivo:

        return len(arquivo.readlines())
    
    except FileNotFoundError:

         print('arquivo não encontrado!!!')


def main()
    
    quatidade_linhas = contar_linhas()

    print(f"o arquivo lido tem (quantidade_linhas) linhas!")


main()

