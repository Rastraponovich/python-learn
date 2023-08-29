import json


def file_read(file_name='contacts.json') -> list:
    try:
        with open(file_name, encoding='utf-8') as file:
            return json.load(file)
    except OSError:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump([], file, sort_keys=True, indent=2)
            return []


def file_write(new_file, file_name='contacts.json') -> bool:
    with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(new_file, file, sort_keys=True, indent=2)
    return True


def contact_save(contact) -> bool:

    contacts = file_read()

    if not [item for item in contacts if item['phone'] == contact['phone']]:
        contacts.append(contact)
        return file_write(contacts)
    return False


def contact_remove(contact_id: int) -> bool:
    contacts = file_read()

    target = [item for item in contacts if item['id'] == contact_id]
    if target:
        contacts.remove(target[0])
        return file_write(contacts)
    return False


def contact_update(contact: dict) -> bool:
    contacts = file_read()

    if contacts:
        target = [item for item in contacts if item['id'] == contact['id']]

        if target:
            target[0].update(contact)
            return file_write(contacts)
        return False

    return False
