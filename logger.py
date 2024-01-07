from date_create import *

def add_contact(file_name, contact):
    with open(file_name, 'a', encoding='UTF-8') as file:
        file.write(contact)

def show_info(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
        # for contact in enumerate:
        for contact in enumerate(contacts_list, 1):
            print(*contact)


def search_contact(file_name, to_print):
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    
    var_search = input('Выберите вариант поиска: ')
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число команды')
            var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) -1

    search = input('Введите данные для поиска: ')

    with open(file_name, 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        print(contacts_list)
    
    found_contacts = list()
    # for contact_str in contacts_list:
    for i, contact_str in enumerate(contacts_list, 1):
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            if to_print == 1:
                print(i, contact_str)
            found_contacts.append(contact_str) 
    return found_contacts

def create_contact():
    name = input_name()
    surname = input_surname()
    patronumik = input_patronumic()
    phone = input_phone()
    adress = input_adress()
    return f'{surname} {name} {patronumik} {phone}\n{adress}\n\n'

def copy_contact(source_file_name):
    found_contacts = search_contact(source_file_name, 0)
    for i, contact_str in enumerate(found_contacts, 1):
        print(i, contact_str)
    index = input_index_to_copy()
    index_int = int(index) -1
    contact = found_contacts[index_int] + "\n\n"
    target_file_name = input_file_name_to_copy()
    add_contact(target_file_name, contact)
