import math

def eh_primo(n):
    """
    Verifica se um número inteiro positivo n é primo.

    Retorna True se n for primo e False caso contrário.
    """

    if n <= 1:
        return False
    
    if n == 2:
        return True

    
    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    
    return True

numero = 101
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")