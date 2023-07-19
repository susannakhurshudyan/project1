from data_create import input_user_data

def input_data():
    name, surname, phone_number, address = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone_number}\n'
                    f'{address}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone_number};{address}\n\n'
                    f'Ваш выбор:'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone_number}\n'
                       f'{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone_number};{address}\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

def print_data():
    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

def delete_data():
    deleted_line = int(input('Введите номер строки: '))
    with open("data_second_variant.csv", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line_number, line in enumerate(lines):
            if line_number != deleted_line:
                file.write(line)
        file.truncate()
    print('Данные успешно удалены!')

def delete_data():
    number = int(input('Введите номер данных: '))
    with open("data_first_variant.csv", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line_number, line in enumerate(lines):
            if line_number != range(number, number + 4):
                file.write(line)
        file.truncate()    
    print('Данные успешно удалены!')
