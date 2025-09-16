lado_1 = (input("informe um numero -> "))
lado_2 = (input("informe um numero -> "))
lado_3 = (input("informe um, numero -> "))

if lado_1 + lado_2 > lado_3 or \
    lado_2 + lado_3 > lado_1 or \
    lado_1 + lado_3 > lado_2:
    print("triangolo valido")

    if lado_1 == lado_2 == lado_3:
        print("triangolo equilatero")
    elif lado_1 == lado_2 or \
        lado_2 == lado_3 or \
        lado_1 == lado_3:
        print("triangulo isosceles")
    elif lado_1 != lado_2 != lado_3:
        print("triangulo escaleno")
    else:
        print("outro tipo")
else: 
    print("triangulo invalido")