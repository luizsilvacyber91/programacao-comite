minha_lista = [1, 2, 3, 4, 5]
minha_lista.reverse()  
print(minha_lista)    


###############################################################################################

minha_lista_original = [1, 2, 3, 4, 5]
lista_invertida_iterador = reversed(minha_lista_original)
lista_invertida = list(lista_invertida_iterador)  
print(lista_invertida)         
print(minha_lista_original) 