import os 

def criar_pasta(nome_pasta):
    os.mkdir('nome_pasta')
    print('Pasta criada com sucesso!')

def main():
    criar_pasta(input('qual da pasta quedeseja criar'))

    main()