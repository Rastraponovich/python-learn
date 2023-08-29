from phonebook.phone_book import PhoneBook
from phonebook.constants import menu_errors_dict


class ConsoleMenu():
    def __init__(self, model=PhoneBook()):
        self.__model = model
        self.__menu_options = {
            1: {'title': 'Get all contacts', 'action': self.__get_all},
            2: {'title': 'Add contact', 'action': self.__create},
            3: {'title': 'Delete contact', 'action': self.__delete},
            4: {'title': 'Search contact', 'action': self.__search},
            5: {'title': 'Update contact', 'action': self.__update},
            6: {'title': 'Exit', 'action': None},
        }

    def __get_all(self):
        contacts_list = self.__model.contacts_get()
        print(list(contacts_list))

    def __update(self):
        contact_id = int(input('ID contact: '))
        name = input('Name: ')
        phone = int(input('Phone: '))

        if self.__model.update_contact({'id': contact_id, 'name': name, 'phone': phone}) is True:
            print('Contact updated')

        else:
            print(f'{menu_errors_dict.get(3)} with id: {contact_id}')

    def __create(self):
        name = input('Name: ')
        phone = int(input('Phone: '))

        if self.__model.contact_add({'name': name, 'phone': phone}) is True:
            print('Contact added')

    def __delete(self):
        contact_id = int(input('ID contact: '))

        if self.__model.contact_remove(contact_id) is True:
            print('Contact removed')

        else:
            print(f'{menu_errors_dict.get(3)} with id: {contact_id}')

    def __search(self):
        search_value = input('Enter search value: ')

        search_result = self.__model.search_contact(search_value)

        if not isinstance(search_result, str):
            print(list(search_result))
        else:
            print(search_result)

    def __print_menu(self):
        """
        Print the menu options.

        This function iterates over the menu options dictionary and prints each option and its title.

        Parameters:
            None

        Returns:
            None
        """
        for item in self.__menu_options.items():
            print(item[0], '--', item[1].get('title'))

    def run(self):
        while True:
            self.__print_menu()

            try:
                option = int(input('Enter your choice: '))
            except ValueError:
                print(menu_errors_dict.get(1))
                continue

            if option == 6:
                print('Thanks message before exiting')
                return

            menu_item = self.__menu_options.get(option)

            if menu_item is None:
                print(
                    f'{menu_errors_dict.get(2)} {len(self.__menu_options)}.')
            else:
                action = menu_item.get('action')

                if action is not None:
                    action()
                else:
                    return
