numero_1 = int(input('informe o primeiro numero -> '))
numero_2 = int(input("informe o segundo numero -> "))
numero_3 = int(input("informe o terceiro numero"))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("o numero", numero_1, "é o maior ")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("os numeros", numero_2, "é o maior")
else:
    print("o numero", numero_3, "é o maior")
