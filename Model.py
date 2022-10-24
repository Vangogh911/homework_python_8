phonebook = []
path = 'phone.txt'


def open_file():
    global phonebook
    global path
    with open(path, "r", encoding="UTF-8") as data:
        phonebook = data.read().split("\n")


def save_file():
    global phonebook
    global path
    with open(path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(phonebook)))


def add_contact():
    global phonebook
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};'
    phonebook.append(contact)
    print_phone_book()


def remove_contact():
    global phonebook
    choice = int(input('Введите номер элемента для удаления: '))
    phonebook.pop(choice)
    print_phone_book()


def change_contact():
    global phonebook
    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))
    contact = phonebook.pop(choice).split(';')
    if choice2 != 0:
        contact[choice2] = " " + input('Введите новое значение: ')
    else:
        contact[choice2] = input('Введите новое значение: ')
    phonebook.insert(choice, ';'.join(contact))
    print_phone_book()


def print_phone_book():
    global phonebook
    [print(i, item) for i, item in enumerate(phonebook)]


def contact_serching():
    task = input('Введите значение для поиска: ')
    count = 0
    for i in phonebook:
        if task in i:
            print(i)
            count += 1
    print(f'\nНайдено {count} контактов')
