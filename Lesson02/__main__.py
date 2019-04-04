import re


result = re.match(r'Изготовитель системы', 'Изготовитель системы:             DELL')

print(result.start())