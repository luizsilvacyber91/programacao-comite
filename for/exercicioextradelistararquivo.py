import os

def listar_arquivo():
    items = os.listdir('.')
    for item in items:
        print(item)


def main():
    listar_arquivo()


main()