def ler_logs(nome_arquivo):

    with open(nome_arquivo , 'r') as arquivo:

        logs = arquivo.readlines()

        resultados = {'info': 0,
                      'error': 0,
                      'warning': 0}
        
        for linha in logs:

            if 'info' in linha:
                resultados['info'] += 1

            elif 'error' in linha:
                resultados['error'] += 1

            elif 'warning' in linha:
                resultados['warning'] += 1

    return resultados

def gerar_relatorio(resultados):

    with open('relatorio.txt', 'w') as arquivo:

        arquivo.write('relatorio de log\n')

        for chave, valor in resultados.items():
            arquivo.write(f'Existem (valor) ocorrencias do log (chave)\n')

    print('Relatorios de logs')

    for chave, valor in resultados.items():
        
        print(f'existem (valor) ocorrencias do log (chave)')

def main():

    nome_arquivo = 'logs_desafio.txt'

    resultados = ler_logs(nome_arquivo)

    gerar_relatorio(resultados)

main()