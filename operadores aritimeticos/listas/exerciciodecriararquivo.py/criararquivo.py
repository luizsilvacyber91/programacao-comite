import logging
import time


logging.basicConfig(
    filename='meu_log.log',  
    level=logging.INFO,      
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'  
)

logging.info('Esta é a primeira mensagem de log.')
time.sleep(1) 
logging.warning('Esta é a segunda mensagem, um aviso ocorreu.')
time.sleep(1)
logging.error('Esta é a terceira mensagem, indicando um erro.')

print("As mensagens foram registradas no arquivo 'meu_log.log'.")