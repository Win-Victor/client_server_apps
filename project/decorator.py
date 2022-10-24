import sys
import logging
import logs.client_log_config
import logs.server_log_config
# import traceback
# import inspect


def log(log_func):
    def wrap_f(*args, **kwargs):
        logger_name = 'client_log' if 'client.py' in sys.argv[0] else 'server_log'
        logger = logging.getLogger(logger_name)

        result = log_func(*args, **kwargs)
        logger.debug(f'Была вызвана функция {log_func.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {log_func.__module__}')
        return result
    return wrap_f
