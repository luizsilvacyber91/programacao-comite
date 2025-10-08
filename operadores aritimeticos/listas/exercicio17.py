from collections import Counter

minha_lista = [1, 2, 3, 2, 4, 1, 2, 5, 2]

quantidade_de_2 = minha_lista.count(2)

print(f"O número 2 aparece {quantidade_de_2} vezes na lista.") 

contagem_completa = Counter(minha_lista)

print(f"A contagem de cada item é: {contagem_completa}") 