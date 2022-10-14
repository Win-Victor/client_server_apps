import logging
import os
import sys

sys.path.append('../')
from common.variables import ENCODING, LOGGING_LEVEL, COMMON_FORMATTER

log = logging.getLogger('client_log')

stream_hand = logging.StreamHandler(sys.stderr)
stream_hand.setLevel(LOGGING_LEVEL)
stream_hand.setFormatter(COMMON_FORMATTER)
log.addHandler(stream_hand)

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')
file_hand = logging.FileHandler(PATH, encoding=ENCODING)
file_hand.setLevel(LOGGING_LEVEL)
file_hand.setFormatter(COMMON_FORMATTER)
log.addHandler(file_hand)
log.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическая ошибка')
