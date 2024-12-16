from queries import add_contact_query, get_all_contacts, delete_contact_query, get_contact, update_contact_query, \
    get_active_user


def add_contact() -> bool:
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")
    user_id = get_active_user()[0]
    if add_contact_query(params=(user_id, full_name, phone_number,)):
        return True
    return False


def show_contacts():
    user_id = get_active_user()[0]
    contacts = get_all_contacts(user_id=user_id)
    message = "Contacts:\n"

    if contacts:
        counter = 1
        for contact in contacts:
            message += f"{counter}. ID: {contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}\n"
            counter += 1
        return message
    else:
        message = "No contacts yet"
        return message


def delete_contact() -> bool | None:
    contact_id = int(input("Enter contact ID: "))
    if get_contact(contact_id=contact_id):
        if delete_contact_query(contact_id=contact_id):
            return True
        else:
            return False


def update_contact():
    contact_id = int(input("Enter contact ID: "))
    if get_contact(contact_id=contact_id):
        new_name = input("Enter new name: ")
        if update_contact_query(contact_id=contact_id, new_name=new_name):
            return True
        else:
            return False
