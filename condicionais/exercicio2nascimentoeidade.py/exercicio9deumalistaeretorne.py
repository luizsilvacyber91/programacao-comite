def remover_duplicatas_com_set(lista_original):
  
  return list(set(lista_original))

lista = [8, 9, 9, 10, 12, 12, 15, 16, 16, 17, 18, 18]

nova_lista = remover_duplicatas_com_set(lista)

print(nova_lista)  