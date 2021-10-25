from car_rent.car.models import CarDatabase
from car_rent.car.menu_option import CarMenu
from car_rent.exceptions import WrongOptionException


def car_app_menu():
    car_db = CarDatabase()  # stworzenie instatcję bazy danych
    car_db.read_car_database()
    car_menu = CarMenu(car_db)

    while True:
        option = input("1 - Add car, 2 - Search car, 3 - Edit car, 4 - Delete car, 5 - Exit: ")

        if option == "1":
            car_menu.add_car()
        if option == "2":
            try:
                car_menu.search_car()
            except WrongOptionException as exception:
                print(exception)
        if option == "3":
            try:
                car_menu.edit_car()
            except WrongOptionException as exception:
                print(exception)
        if option == "4":
            try:
                car_menu.delete_car()
            except WrongOptionException as exception:
                print(exception)
        if option == "5":
            print("Exit to the main menu")
            break

    car_db.save_database()
