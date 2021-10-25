from car_rent.client.models import ClientDatabase
from car_rent.client.menu_option import ClientMenu
from car_rent.exceptions import WrongOptionException


def client_app_menu():
    client_db = ClientDatabase()
    client_db.read_client_database()
    client_menu = ClientMenu(client_db)

    while True:
        option = input("1 - Add client, 2 - Search client, 3 - Edit client, 4 - Delete client, 5 - Exit: ")

        if option == "1":
            client_menu.add_client()
        if option == "2":
            try:
                client_menu.search_client()
            except WrongOptionException as exception:
                print(exception)
        if option == "3":
            try:
                client_menu.edit_client()
            except WrongOptionException as exception:
                print(exception)
        if option == "4":
            try:
                client_menu.delete_client()
            except WrongOptionException as exception:
                print(exception)
        if option == "5":
            print("Exit to the main menu")
            break

    client_db.save_database()
