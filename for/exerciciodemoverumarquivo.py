import shutil
import os

caminho_origem = "/caminho/para/seu/arquivo/origem.txt"

caminho_destino = "/caminho/para/sua/pasta/destino/"

if os.path.exists(caminho_origem):

    try:
        
        shutil.move(caminho_origem, caminho_destino)

        print(f"Arquivo '{caminho_origem}' movido para '{caminho_destino}' com sucesso.")

    except Exception as e:

        print(f"Erro ao mover o arquivo: {e}")

else:
    
    print(f"Arquivo de origem não encontrado em '{caminho_origem}'.")