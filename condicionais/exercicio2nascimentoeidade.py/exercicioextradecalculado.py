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

def main():
    continuar = True
    while continuar:
        numero1 = float(input("informe o primeiro valor -> "))
        numero2 = float(input("informe o segundo valor -> "))
        operação = input("informe a operação -> ")

        resultado = calculadora(numero1, numero2, operação)
        if resultado != None:
              print(f"{numero1} {operação} {numero2} = {resultado}")

        continuar = input("Deseja continuar? 'S' ou 'N' -> ")
        if continuar == "s":
              continuar = True
        elif continuar == "n":
              continuar = False
        else:
              print("opção invalida!")
              continue
        
main()
              
