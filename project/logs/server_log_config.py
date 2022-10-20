import logging
import logging.handlers
import os
import sys

sys.path.append('../')
from common.variables import ENCODING, LOGGING_LEVEL, COMMON_FORMATTER

log = logging.getLogger('server_log')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

stream_hand = logging.StreamHandler(sys.stderr)
stream_hand.setLevel(LOGGING_LEVEL)
stream_hand.setFormatter(COMMON_FORMATTER)

rotation_log_handler = logging.handlers.TimedRotatingFileHandler(PATH, encoding=ENCODING, interval=1, when='D')
rotation_log_handler.setFormatter(COMMON_FORMATTER)
rotation_log_handler.setLevel(LOGGING_LEVEL)

log.setLevel(logging.DEBUG)
log.addHandler(stream_hand)
log.addHandler(rotation_log_handler)

if __name__ == '__main__':
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическая ошибка')
