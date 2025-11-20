def abrir_arquivo_com_tratamento(nome_arquivo):
    """
    Tenta abrir um arquivo e trata a exceção FileNotFoundError se ele não existir.
    """
    try:
        
        with open(nome_arquivo, 'r') as arquivo:

            print(f"Arquivo '{nome_arquivo}' aberto com sucesso.")
            

    except FileNotFoundError as e:
        
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        print(f"Detalhes do erro: {e}")
        print("Por favor, verifique se o nome ou o caminho do arquivo está correto.")

    except Exception as e:
        
        print(f"Ocorreu um erro inesperado: {e}")

    else:
        
        print("Operação de abertura e leitura do arquivo concluída sem erros.")

    finally:
        
        print("Fim da tentativa de acesso ao arquivo.")

nome_do_arquivo_inexistente = "arquivo_secreto_inexistente.txt"

print(f"Tentando abrir o arquivo: {nome_do_arquivo_inexistente}\n")

abrir_arquivo_com_tratamento(nome_do_arquivo_inexistente)

print("-" * 30)
