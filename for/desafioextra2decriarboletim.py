def gerar_boletim(aluno):
    with open('boletim.txt', 'w') as boletim:
        for chave, valor in aluno.items():
            if type(valor) !=float:
                boletim.write(f'{chave}| {valor}\n')
            
            else:
                boletim.write(f'{chave}| {valor:.2f}\n')

    for chave, valor in aluno.items():
        if type(valor) != float:
            print(f'{chave}| {valor}')

def calcular_boletim(aluno):
    media = (aluno['nota_1'] + aluno['nota_2'] + aluno['nota_3']) /3
    status_aluno = ''
    if media >= 7:
        status_aluno = 'aprovado'
    else:
        status_aluno = 'reprovado'

    aluno.update({'media': media,
                  'status_aluno': status_aluno})
    
    gerar_boletim(aluno)

def obtem_info():


    aluno = {'nome':'',
             'nota_1': 0,
             'nota_2': 0,
             'nota_3': 0}
    
    aluno['nome'] = input('informe o nome do aluno -> ')
    aluno['nota_1'] = float(input('informe a primeira nota -> '))
    aluno['nota_2'] = float(input('informe a segunda nota -> '))
    aluno['nota_3'] = float(input('informe a terceira nota -> '))

    return aluno

def main():
    aluno = obtem_info()
    calcular_boletim(aluno)

main()