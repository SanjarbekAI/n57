import menu_text
from Projects.contacts.auth import register, activate_email, login
from crud import add_contact, show_contacts, delete_contact, update_contact
from queries import create_tables, logout_all


def show_auth_menu():
    print(menu_text.auth_menu)
    option = input("Enter your option: ")
    if option == "1":
        if register():
            print("Check your email, we sent a verification code. Activate your email by menu 4")
        else:
            print("Something went wrong")
    elif option == "2":
        if login():
            print("Welcome to main menu")
            return show_main_menu()
    elif option == "3":
        pass
    elif option == "4":
        activate_email()
    elif option == "5":
        pass
    else:
        print("Invalid option")
    return show_auth_menu()


def show_main_menu():
    print(menu_text.main_menu)
    option = input("Enter your option: ")

    if option == "1":
        if add_contact():
            print("New contact added")
        else:
            print("Something went wrong")
    elif option == "2":
        result = delete_contact()
        if result is True:
            print("Deleted contact")
        elif result is False:
            print("Something went wrong")
        else:
            print("Contact not found")
    elif option == "3":
        result = update_contact()
        if result is True:
            print("Contact updated")
        elif result is False:
            print("Something went wrong")
        else:
            print("Contact not found")
    elif option == "4":
        result = show_contacts()
        print(result)
    elif option == "5":
        pass
    else:
        print("Invalid option")
    return show_main_menu()


if __name__ == "__main__":
    create_tables()
    logout_all()
    show_auth_menu()
