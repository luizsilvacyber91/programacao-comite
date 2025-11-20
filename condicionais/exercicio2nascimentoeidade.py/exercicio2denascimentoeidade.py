import datetime

def calcular_idade(ano_nascimento):
  """
  Calcula a idade com base no ano de nascimento.

  Argumentos:
    ano_nascimento: o ano de nascimento (inteiro)

  Retorna:
    a idade (inteiro)
  """
  ano_atual = datetime.date.today().year

  idade = ano_atual - ano_nascimento

  return idade

ano = 1925

idade_calculada = calcular_idade(ano)

print(f"Você tem {idade_calculada} anos.")


#######################################################################################

