import sys
import locale


data = [
    'программирование',
    'сокет',
    'декоратор'
]

file = open('lesson01/test_file.txt', 'w')

for text in data:
    print(text)
    file.write(text + ' ')
file.close()

print('Кодировка по умолчанию - ' + locale.getpreferredencoding())

# Попытка открыть в формате Unicode
try:
    with open('lesson01/test_file.txt', encoding='utf-8') as file:
        for text in file:
            print(text)
except:
    print(sys.exc_info()[1])