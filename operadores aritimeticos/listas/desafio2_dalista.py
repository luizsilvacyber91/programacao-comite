
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lista_pares = []


for numero in lista_numeros:
  
  if numero % 2 == 0:
    
    lista_pares.append(numero)


print("Lista original:", lista_numeros)
print("Lista de números pares:", lista_pares)