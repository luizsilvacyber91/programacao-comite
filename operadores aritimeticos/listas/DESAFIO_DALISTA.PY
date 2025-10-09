
numeros = [2, 5, 8, 10, 11]

for i in range(5):

        numeros.append(int(input(f"informe o {i+1}º numero -> ")))
    
print(f"os numeros digitados foram ", end=" ")

for i in numeros:
    
    print(i, end=" ")

print(f"\no maior numero digitado foi {max(numeros)}")
print(f"o menor numero digitado foi{min(numeros)}")
print(f"a media dos numeros é {sum(numeros)/len(numeros)}")

            
           