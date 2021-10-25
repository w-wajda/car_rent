from car_rent.car.app import car_app_menu
from car_rent.client.app import client_app_menu
from car_rent.lease_contract.app import lease_contract_menu

while True:
    print("Make your choice")
    option = input("1 - Car, 2 - client, 3 - Lease Contract, 4 - Exit: ")

    if option == '1':
        print("What you want to do? ")
        car_app_menu()

    if option == '2':
        print("What you want to do? ")
        client_app_menu()

    if option == '3':
        print("What you want to do? ")
        lease_contract_menu()

    if option == '4':
        print("The program closed")
        break
