
resultado = "Este é o conteúdo do relatório a ser salvo no arquivo."

outro_dado = "Aqui está uma linha adicional de dados."

nome_arquivo = "relatorio.txt"

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        
        arquivo.write(resultado + "\\n") 

        arquivo.write(outro_dado + "\\n") 
    
    print(f"O resultado foi salvo com sucesso no arquivo '{nome_arquivo}'.")

except IOError as e:
    
    print(f"Ocorreu um erro ao escrever no arquivo: {e}")