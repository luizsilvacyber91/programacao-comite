def boletim(nome, nota1, nota2, nota3):
  """
  Calcula a média de três notas e determina a situação (aprovado/reprovado).

  Args:
    nome (str): O nome do aluno.
    nota1 (float): A primeira nota.
    nota2 (float): A segunda nota.
    nota3 (float): A terceira nota.

  Returns:
    dict: Um dicionário com o nome, a média e a situação do aluno.
  """
  media = (nota1 + nota2 + nota3) / 3
  
  if media >= 6.0: 
    situacao = "Aprovado"
  else:
    situacao = "Reprovado"

  return {
      "nome": nome,
      "media": round(media, 2), 
      "situacao": situacao
  }

aluno1 = boletim("Alice", 9.5, 8.0, 6.5)
print(aluno1)

aluno2 = boletim("Bob", 4.0, 6.5, 7.0)
print(aluno2)