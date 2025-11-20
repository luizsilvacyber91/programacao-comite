import re

def contar_logs(nome_arquivo):
    """
    Lê um arquivo e conta as ocorrências de INFO, ERROR e WARNING.
    """
    contagens = {
        'INFO': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    
    try:
        with open(nome_arquivo, 'r', encoding='meu_arquivo_copia.txt) as arquivo'):
            for linha in arquivo:
                
                if re.search(r'\bINFO\b', linha, re.IGNORECASE):
                    contagens['INFO'] += 1
                if re.search(r'\bERROR\b', linha, re.IGNORECASE):
                    contagens['ERROR'] += 1
                if re.search(r'\bWARNING\b', linha, re.IGNORECASE):
                    contagens['WARNING'] += 1
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None
        
    return contagens

if __name__ == "__main__":
    
    nome_do_arquivo = 'meu_arquivo_copia.txt' 
    
    resultados = contar_logs(nome_do_arquivo)
    
    if resultados:
        print(f"--- Resultado da Contagem em '{nome_do_arquivo}' ---")
        print(f"INFO:    {resultados['INFO']}")
        print(f"ERROR:   {resultados['ERROR']}")
        print(f"WARNING: {resultados['WARNING']}")