import os

nome_da_pasta = "minha_nova_pasta"

if not os.path.exists(nome_da_pasta):
    
    os.mkdir(nome_da_pasta)
    
    print(f"A pasta '{nome_da_pasta}' foi criada com sucesso!")
else:
    print(f"A pasta '{nome_da_pasta}' já existe.")