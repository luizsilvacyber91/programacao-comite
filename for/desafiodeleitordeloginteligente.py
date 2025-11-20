def processar_log(nome_arquivo):
    """
    Processa um arquivo de log para encontrar e contar linhas de erro.
    """
    contador_erros = 0
    print(f"Iniciando o processamento do arquivo: {nome_arquivo}")

    try:
        
        with open(nome_arquivo, 'r') as arquivo:
            for numero_linha, linha in enumerate(arquivo, 1):
                
                linha = linha.strip()
                
                if "ERROR" in linha.upper():
                    
                    contador_erros += 1

                    print(f"[ERRO na Linha {numero_linha}]: {linha}")

    except FileNotFoundError:

        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

        return
    
    except Exception as e:

        print(f"Ocorreu um erro durante a leitura do arquivo: {e}")

        return

    print(f"\nProcessamento concluído.")

    print(f"Total de linhas de erro encontradas: {contador_erros}")

nome_do_seu_arquivo = "meu_log.txt"