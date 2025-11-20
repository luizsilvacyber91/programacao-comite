def contar_numeros_positivos(lista_de_numeros):
   
    contador = 0  

    for numero in lista_de_numeros:
        
        if numero > 0:
            contador += 1  
    return contador

minha_lista = [10, -5, 2, 0, -8, 4, 1, -3]

quantidade = contar_numeros_positivos(minha_lista)

print(f"A lista é: {minha_lista}")
print(f"O número de elementos positivos na lista é: {quantidade}")
