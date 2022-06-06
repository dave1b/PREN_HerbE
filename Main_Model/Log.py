import logging
import sys


class Logger:
    def __init__(self, name=""):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(name)s --- %(message)s",
            handlers=[
                logging.FileHandler("HerbE.log"),
                logging.StreamHandler(sys.stdout)
            ])
        self.logging = logging.getLogger(name)

    def debug(self, message):
        self.logging.debug(message)

    def info(self, message):
        self.logging.info(message)

    def warning(self, message):
        self.logging.warning(message)

    def error(self, message):
        self.logging.error(message)
