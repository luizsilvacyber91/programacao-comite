def boletim(nome, n1, n2, n3):
    
    media = (n1 + n2 + n3) / 3

    if media >= 7.0:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'

    return {
        'nome': nome,
        'media': round(media, 2), 
        'situacao': situacao
    }

aluno1 = boletim("Maria", 8.5, 7.0, 9.2)
aluno2 = boletim("João", 5.0, 6.5, 4.0)

print(aluno1)
print(aluno2)