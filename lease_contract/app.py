from car_rent.car.models import CarDatabase
from car_rent.client.models import ClientDatabase
from car_rent.exceptions import WrongOptionException

from car_rent.lease_contract.models import LeaseContractDatabase
from car_rent.lease_contract.menu_option import LeaseContractMenu


def lease_contract_menu():
    car_db = CarDatabase()
    car_db.read_car_database()

    client_db = ClientDatabase()
    client_db.read_client_database()

    lc_db = LeaseContractDatabase()
    lc_db.read_lease_contract_database()

    lc_menu = LeaseContractMenu(lc_db, car_db, client_db)

    while True:
        question = input("1 - Add lease contract, 2 - Search lease contract, 3 - Edit lease contract, "
                         "4 - Delete lease contract, 5 - Exit: ")

        if question == "1":
            lc_menu.add_lease_contract()
        if question == "2":
            try:
                lc_menu.search_lease_contract()
            except WrongOptionException as exception:
                print(exception)
        if question == "3":
            try:
                lc_menu.edit_lease_contract()
            except WrongOptionException as exception:
                print(exception)
        if question == "4":
            try:
                lc_menu.delete_lease_contract()
            except WrongOptionException as exception:
                print(exception)
        if question == "5":
            print("Close the program")
            break

    car_db.save_database()
    client_db.save_database()
    lc_db.save_database()

