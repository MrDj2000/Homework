import sys
import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Определить формат сообщений
format = logging.Formatter('%(asctime)s %(levelname)-10s %(module)-15s %(message)s')

file_path = os.getcwd()
file_name = 'server\log\server.log'

# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.WARNING)
crit_hand.setFormatter(format)

# Создать обработчик, который выводит сообщения в файл
applog_hand = TimedRotatingFileHandler(filename=os.path.join(file_path, file_name), when='D', interval=1, encoding='utf8')
applog_hand.setFormatter(format)

# Создать регистратор верхнего уровня с именем 'server'
app_log = logging.getLogger('server')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

# Изменить уровень важности для регистратора 'server.net'
logging.getLogger('server.net').setLevel(logging.ERROR)
