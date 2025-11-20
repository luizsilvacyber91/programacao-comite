def obtem_valor():
    return int(input('informe um valor -> '))

def main():
    try:
        valor = obtem_valor()
    except ValueError:
        print('valor invalido!', end=' ')
        print('necessario ser um numero inteiro!')

    else:
        print(f'valor informado e (valor)')

main()