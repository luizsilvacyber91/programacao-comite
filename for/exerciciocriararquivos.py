for i in range(1, 6):
    
    nome_arquivo = f"arq{i}.txt"
    
    with open(nome_arquivo, 'w') as f:
        
        f.write(f"Este é o arquivo de número {i}.")
    
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")