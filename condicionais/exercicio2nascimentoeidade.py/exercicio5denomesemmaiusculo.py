def converter_para_maiusculas(lista_de_nomes):
  
  nomes_maiusculos = []

  for nome in lista_de_nomes:

    nomes_maiusculos.append(nome.upper())

  return nomes_maiusculos

nomes_originais = ["Ana", "bruno", "Carlos", "diana"]

nomes_convertidos = converter_para_maiusculas(nomes_originais)

print(f"Lista original: {nomes_originais}")

print(f"Lista em maiúsculas: {nomes_convertidos}")