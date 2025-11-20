

import json

def ler_e_imprimir_json(nome_arquivo):
    """
    Lê um arquivo JSON e imprime seus valores.
    """
    try:
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            dados = json.load(arquivo)
            
            print(f"Conteúdo do arquivo '{nome_arquivo}':")
            
            if isinstance(dados, dict):

                for chave, valor in dados.items():

                    print(f"- {chave}: {valor}")
            
            elif isinstance(dados, list):

                for item in dados:

                    print(f"- {item}")
            else:
            
                print(f"Valor: {dados}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o arquivo JSON. Verifique a sintaxe do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

nome_do_arquivo = 'dados.json'

ler_e_imprimir_json(nome_do_arquivo)