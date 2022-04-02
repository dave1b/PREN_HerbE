import logging
import sys

class Logger:
    def __init__(self):
        logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] ---- %(message)s",
        handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
        ])
        
    def debug(self, message):
        logging.debug(message)
    def info(self, message):
        logging.info(message)
    def warning(self, message):
        logging.warning(message)
    def error(self, message):
        logging.error(message)
    
#logging.debug('This message is skipped as a level is set as INFO')
#logging.info('So should this')
#logging.warning('And this, too')
#logging.error('Testing non-ASCII character, Ø and ö')