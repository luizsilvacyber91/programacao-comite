import shutil
import os

origem = 'meu_arquivo.txt'

destino = 'meu_arquivo_copia.txt'

try:
    
    with open(origem, 'w') as f:

        f.write("Conteúdo de exemplo do arquivo original.\n")

    shutil.copy(origem, destino)

    print(f"Arquivo copiado com sucesso de '{origem}' para '{destino}'")

    if os.path.exists(destino):

        print(f"O arquivo '{destino}' foi criado e pode ser acessado.")

    else:

        print(f"A cópia falhou.")

except FileNotFoundError:

    print(f"Erro: O arquivo de origem '{origem}' não foi encontrado.")

except Exception as e:
    
    print(f"Ocorreu um erro: {e}")