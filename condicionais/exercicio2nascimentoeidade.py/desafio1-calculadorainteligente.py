def calculadora(numero1, numero2, operacao):

    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida." 
    else:
        return "Erro: Operação inválida. Use '+', '-', '*', ou '/'." 

resultado_soma = calculadora(20, 5, '+')
print(f"20 + 5 = {resultado_soma}")

resultado_subtracao = calculadora(40, 8, '-')
print(f"40 - 8 = {resultado_subtracao}")

resultado_multiplicacao = calculadora(6, 5, '*')
print(f"6 * 5 = {resultado_multiplicacao}")

resultado_divisao = calculadora(100, 10, '/')
print(f"100 / 10 = {resultado_divisao}")
      
resultado_divisao_zero = calculadora(50, 0, '/')
print(f"50 / 0 = {resultado_divisao_zero}")

resultado_invalido = calculadora(15, 5, '%')
print(f"15 % 5 = {resultado_invalido}")

def somar(a, b):
    resultado = a + b
    return resultado

num1 = 20
num2 = 5
soma = somar(num1, num2)
print(f"O resultado da soma é: {soma}")
