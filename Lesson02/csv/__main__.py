import csv
import re

v_header = 'Lesson02/'

def get_data():

    v_files = [
        'info_1.txt',
        'info_2.txt',
        'info_3.txt',
    ]

    v_params = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]

    main_data = [v_params]

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for f_file in v_files:

        v_prod_list = ''
        v_name_list = ''
        v_code_list = ''
        v_type_list = ''

        with open(f'{v_header}in/' + f_file) as file:
            reader = csv.reader(file)
            for f_row in reader:
                v_row = str(''.join(f_row))
                for f_params in range(len(v_params)):
                    v_re = re.compile(fr'({v_params[f_params]}:)(\s+)(.+)').findall(v_row)
                    if v_re:
                        for f_result in v_re:
                            if f_params == 0:
                                v_prod_list = f_result[2]
                            elif f_params == 1:
                                v_name_list = f_result[2]
                            elif f_params == 2:
                                v_code_list = f_result[2]
                            elif f_params == 3:
                                v_type_list = f_result[2]

        main_data.append([v_prod_list, v_name_list, v_code_list, v_type_list])
        os_prod_list.append(v_prod_list)
        os_name_list.append(v_name_list)
        os_code_list.append(v_code_list)
        os_type_list.append(v_type_list)
#       print('The End ' + f_file)

#    print(*main_data)
#    print(os_prod_list)
#    print(os_name_list)
#    print(os_code_list)
#    print(os_type_list)
#    print('The End')

    return main_data

def write_csv():

    main_data = get_data()

    with open(f'{v_header}csv/main_data.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(main_data)

write_csv()