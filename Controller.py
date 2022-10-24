import Model
import View


def main_menu():
    while True:
        View.menu()
        match View.choice:
            case 0:
                Model.print_phone_book()
            case 1:
                Model.open_file()
                print('\nФайл открыт')
            case 2:
                Model.save_file()
                print('\nФайл сохранен')
            case 3:
                Model.add_contact()
                print('\nКонтакт добавлен')
            case 4:
                Model.change_contact()
            case 5:
                Model.remove_contact()
                print('\nКонтакт удален')
            case 6:
                Model.contact_serching()
            case 7:
                break


def start():
    Model.open_file()
    Model.print_phone_book()
    main_menu()
