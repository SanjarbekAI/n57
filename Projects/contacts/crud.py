from queries import add_contact_query, get_all_contacts


def add_contact() -> bool:
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")

    if add_contact_query(params=(full_name, phone_number,)):
        return True
    return False


def show_contacts():
    contacts = get_all_contacts()
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
