import os

caminho_atual = os.getcwd()

todos_itens = os.listdir(caminho_atual)

arquivos_na_pasta = [item for item in todos_itens if os.path.isfile(os.path.join(caminho_atual, item))]

print("Arquivos na pasta atual:")

for arquivo in arquivos_na_pasta:
    
    print(arquivo)