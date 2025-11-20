import os

nome_do_arquivo = "outro_arquivo.txt"

try:
    os.remove(nome_do_arquivo)
    print(f"O arquivo '{nome_do_arquivo}' foi apagado com sucesso.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
except PermissionError:
    print(f"Erro: Você não tem permissão para apagar o arquivo '{nome_do_arquivo}'.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")