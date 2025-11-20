def unir_arquivos(arquivo1_nome, arquivo2_nome, arquivo_destino_nome):
    """
    Lê o conteúdo de dois arquivos e escreve em um terceiro.
    """
    try:
        
        with open(arquivo1_nome, 'r', encoding='utf-8') as f1:
            conteudo1 = f1.read()
        
        with open(arquivo2_nome, 'r', encoding='utf-8') as f2:
            conteudo2 = f2.read()
        
        with open(arquivo_destino_nome, 'w', encoding='utf-8') as fd:
            fd.write(conteudo1)
            fd.write(conteudo2)
            print(f"Conteúdo de '{arquivo1_nome}' e '{arquivo2_nome}' foi unido em '{arquivo_destino_nome}' com sucesso.")

    except FileNotFoundError as e:
        print(f"Erro: Um dos arquivos não foi encontrado. {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

unir_arquivos('arquivo1.txt', 'arquivo2.txt', 'arquivo_final.txt')