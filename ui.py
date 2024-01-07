from logger import *


def interface():
    file_name = 'phonebook.txt'
    with open(file_name, 'r', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта\n'
            '5. Выход из программы')
    
        command = input('Введите номер действия: ')
    
        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число команды')
            command = input('Введите номер действия: ')
    
        match command:
            case '1':
                add_contact(file_name, create_contact())
            case '2':
                show_info(file_name)
            case '3':
                search_contact(file_name, 1)
            case '4':
                copy_contact(file_name)
            case '5':
                print('Всего хорошего! ')
