
from phonebook.service import file_read, contact_remove, contact_save, contact_update


class PhoneBook:
    def __init__(self):
        '''initialize'''
        self.__contacts = file_read()

    def contact_add(self, contact: dict) -> bool:
        '''Create a contact'''

        contact.update({'id': len(self.__contacts) + 1})

        if contact_save(contact) is True:
            self.__contacts = file_read()
            return True
        return False

    def contacts_get(self):
        '''Get All contacts'''
        return self.__contacts

    def contact_remove(self, contact_id: int) -> bool:
        '''Remove contact'''

        if contact_remove(contact_id) is True:
            self.__contacts = file_read()
            return True
        return False

    def contacts_count(self):
        '''Get contacts count'''
        return len(self.__contacts)

    def update_contact(self, contact: dict) -> bool:
        '''Update contact'''

        if contact_update(contact) is True:
            self.__contacts = file_read()
            return True
        return False

    def search_contact(self, search_value) -> list or str:
        '''Search contact by value'''
        search_result = [
            x for x in self.__contacts if
            search_value.lower() in x['name'].lower() or
            search_value.lower() in str(x['phone'])
        ]

        if not search_result:
            return 'Contacts not found'

        return search_result
