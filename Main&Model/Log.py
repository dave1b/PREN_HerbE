

import logging
logger = logging.getLogger('HerbE-Logger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('HerbE.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

#logger.debug('DebugNachricht')
#logger.info('InfoNachricht')
#logger.warning('Warnhinweis')
#logger.error('Fehlermeldung')
#logger.critical('Schwerer Fehler')