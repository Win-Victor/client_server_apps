import sys
import logging
import logs.client_log_config
import logs.server_log_config
import traceback
import inspect


def log(log_func):
    def wrap_f(*args, **kwargs):
        logger_name = 'client_log' if 'client.py' in sys.argv[0] else 'server_log'
        logger = logging.getLogger(logger_name)

        result = log_func(*args, **kwargs)
        logger.debug(f'Была вызвана функция {log_func.__name__} c параметрами {args}, {kwargs}.'
                     f'Вызов из модуля {log_func.__module__}.'
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}'
                     f'Вызов из функции {sys._getframe().f_back.f_code.co_name}'
                     f'Вызов из модуля {sys._getframe().f_back.f_code.co_filename.split("/")[-1]}')
        return result
    return wrap_f
