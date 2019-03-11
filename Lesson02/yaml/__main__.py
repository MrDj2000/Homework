import yaml

file_path = 'lesson02/yaml/file.yaml'

data = {
    'Строка раз': ['Один', 'Два', 'Три'],
    'Строка два': 1,
    'Строка три': {
        1: u'€',
        2: u'¥',
        3: u'Ω'
    }
}

print(data)

with open(file_path, 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=True, allow_unicode=True,)

with open(file_path, encoding='utf-8') as file:
    v_temp = yaml.load(file)
    print(v_temp)
    if v_temp == data:
        print('Данные совпадают!')
    else:
        print('Данные отличаются!')