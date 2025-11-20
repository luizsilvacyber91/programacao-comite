def saudacao_formatada(nome, idade):
 
  return f"Olá, meu nome é {nome} e eu tenho {idade} anos de idade."

nome_usuario = "Marcia"

idade_usuario = 56

frase = saudacao_formatada(nome_usuario, idade_usuario)

print(frase)

print(saudacao_formatada("gislaine", 45))
