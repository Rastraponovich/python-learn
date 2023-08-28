#!/usr/bin/python3
from phonebook.phone_book import PhoneBook

menu_errors_dict = {
    1: 'Only numbers are allowed',
    2: 'Invalid option. Please enter a number between 1 and',
    3: 'Contact not found',
    999: 'Internal error',
}

phone_book = PhoneBook()


def print_menu():
    """
    Print the menu options.

    This function iterates over the menu options dictionary and prints each option and its title.

    Parameters:
        None

    Returns:
        None
    """
    for item in menu_options.items():
        print(item[0], '--', item[1].get('title'))


def contacts_get():
    contacts_list = phone_book.contacts_get()
    print(list(contacts_list))


def contact_update():
    contact_id = int(input('ID contact: '))
    name = input('Name: ')
    phone = int(input('Phone: '))

    if phone_book.update_contact({'id': contact_id, 'name': name, 'phone': phone}) is True:
        print('Contact updated')

    else:
        print(f'{menu_errors_dict.get(3)} with id: {contact_id}')


def contact_add():
    name = input('Name: ')
    phone = int(input('Phone: '))

    if phone_book.contact_add({'name': name, 'phone': phone}) is True:
        print('Contact added')


def contact_delete():
    contact_id = int(input('ID contact: '))

    if phone_book.contact_remove(contact_id) is True:
        print('Contact removed')

    else:
        print(f'{menu_errors_dict.get(3)} with id: {contact_id}')


def contact_search():
    search_value = input('Enter search value: ')

    search_result = phone_book.search_contact(search_value)

    if not isinstance(search_result, str):
        print(list(search_result))
    else:
        print(search_result)


menu_options = {
    1: {'title': 'Get all contacts', 'action': contacts_get},
    2: {'title': 'Add contact', 'action': contact_add},
    3: {'title': 'Delete contact', 'action': contact_delete},
    4: {'title': 'Search contact', 'action': contact_search},
    5: {'title': 'Update contact', 'action': contact_update},
    6: {'title': 'Exit', 'action': None},
}


def console_menu():
    while True:
        print_menu()

        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print(menu_errors_dict.get(1))
            continue

        if option == 6:
            print('Thanks message before exiting')
            return

        menu_item = menu_options.get(option)

        if menu_item is None:
            print(
                f'{menu_errors_dict.get(2)} {len(menu_options)}.')
        else:
            action = menu_item.get('action')

            if action is not None:
                action()
            else:
                return


console_menu()
