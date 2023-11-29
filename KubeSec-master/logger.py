import logging
from datetime import date

def createLogger() -> logging.Logger:
    filename = str(date.today()) + '.log'
    
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=filename, level=logging.info)
    return logging.Logger('KubeSec Main Logger')