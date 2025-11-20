nome_do_arquivo = 'seu_arquivo.txt'

try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        lista_de_linhas = arquivo.readlines()
    
    
    lista_processada = [linha.strip() for linha in lista_de_linhas]

    print("Conteúdo do arquivo na lista original (com \\n):")
    print(lista_de_linhas)
    print("\nConteúdo do arquivo na lista processada (sem \\n):")
    print(lista_processada)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")