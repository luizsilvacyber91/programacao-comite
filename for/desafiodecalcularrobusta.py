def calculadora():
    """
    Função que implementa uma calculadora com 4 operações e tratamento de erros.
    """
    print("Calculadora Python. Digite 'sair' a qualquer momento para fechar.")

    
    while True:
        
        while True:
            entrada1 = input("Digite o primeiro valor: ")
            if entrada1.lower() == 'sair':
                return 
            try:
                num1 = float(entrada1)
                break 
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número válido ou 'sair'.")

        
        while True:
            entrada2 = input("Digite o segundo valor: ")
            if entrada2.lower() == 'sair':
                return
            try:
                num2 = float(entrada2)
                break 
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número válido ou 'sair'.")

        
        while True:
            operacao = input("Digite a operação (+, -, *, /): ")
            if operacao.lower() == 'sair':
                return
            if operacao in ('+', '-', '*', '/'):
                break 
            else:
                print("Erro: Operação inválida. Por favor, digite +, -, *, / ou 'sair'.")

        
        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError 
                resultado = num1 / num2
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            continue 
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            continue

        
        print(f"\nResultado da operação {num1} {operacao} {num2} = {resultado}\n")

if __name__ == "__main__":
    calculadora()
