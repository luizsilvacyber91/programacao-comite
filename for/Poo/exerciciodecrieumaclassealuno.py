class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

aluno_exemplo = Aluno(nome="João", nota1=7.5, nota2=8.5)

print(f"Nome do aluno: {aluno_exemplo.nome}")
print(f"Nota 1: {aluno_exemplo.nota1}")
print(f"Nota 2: {aluno_exemplo.nota2}")

media_do_aluno = aluno_exemplo.calcular_media()
print(f"Média calculada: {media_do_aluno}")

aluno_mariana = Aluno(nome="Mariana", nota1=6.0, nota2=9.0)
print(f"\nAluno: {aluno_mariana.nome}, Média: {aluno_mariana.calcular_media()}")