import logging
import os
import sys

sys.path.append('../')
from common.variables import ENCODING, LOGGING_LEVEL, COMMON_FORMATTER

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

stream_hand = logging.StreamHandler(sys.stderr)
stream_hand.setFormatter(COMMON_FORMATTER)
stream_hand.setLevel(logging.ERROR)
log_file = logging.FileHandler(PATH, encoding=ENCODING)
log_file.setFormatter(COMMON_FORMATTER)
log_file.setLevel(logging.ERROR)

logger = logging.getLogger('client_log')
logger.addHandler(stream_hand)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')
    logger.warning('Предупреждение')
    logger.error('Ошибка')
    logger.critical('Критическая ошибка')
