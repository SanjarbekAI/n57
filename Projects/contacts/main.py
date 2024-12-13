import menu_text
from Projects.contacts.crud import add_contact
from queries import create_tables


def show_main_menu():
    print(menu_text.main_menu)
    option = input("Enter your option: ")

    if option == "1":
        if add_contact():
            print("New contact added")
        else:
            print("Something went wrong")

    elif option == "2":
        pass

    elif option == "3":
        pass

    elif option == "4":
        pass

    elif option == "5":
        pass

    else:
        print("Invalid option")
    return show_main_menu()


if __name__ == "__main__":
    create_tables()
    show_main_menu()