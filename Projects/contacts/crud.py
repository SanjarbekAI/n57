from Projects.contacts.queries import add_contact_query


def add_contact() -> bool:
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")

    if add_contact_query(params=(full_name, phone_number,)):
        return True
    return False
