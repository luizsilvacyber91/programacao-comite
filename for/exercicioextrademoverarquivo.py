from shutil import move

def mover_arquivo():

    move('log,txt', 'Docs/log.txt')

def main():

    mover_arquivo()

main()