choice = 0


def menu():
    global choice
    print('\nГлавное меню:')
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    print('7. Выйти из программы')
    choice = int(input('Выберите пункт: '))
