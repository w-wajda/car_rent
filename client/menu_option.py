from car_rent.client.models import (
    Client,
    ClientDatabase,
)
from car_rent.exceptions import WrongOptionException


class ClientMenu:
    """ TODO: zrobić mixiny per add, search itp."""

    def __init__(self, client_db: ClientDatabase):
        self.client_db = client_db

    @staticmethod
    def shows_the_details_clients(clients):
        for client in clients:
            print(client.get_details())

    @staticmethod
    def set_client_detail(client, field):
        new_value = input(f"Give new {field}: ")
        setattr(client, field, new_value)  # zmienia wartość atrybutu obiektu

    def get_clients_by_input_last_name(self):
        get_last_name = input("Enter your last name: ")
        clients = self.client_db.find_all_item_in_database(get_last_name)
        return clients

    def client_select(self):
        try:
            client_id = int(input("Enter the client id to remove: "))
        except ValueError:
            pass
        else:
            client = self.client_db.get_item_by_id_in_database(client_id)
            return client

    def add_client(self):
        client = Client.create_client()
        self.client_db.add_item(client)
        print("client added")

    def search_client(self):
        clients = self.get_clients_by_input_last_name()
        if not clients:
            raise WrongOptionException("No client in the database")

        try:
            to_add = int(input("Do you want add a client? 1 - YES, 2 - NO: "))
        except ValueError:
            raise WrongOptionException('You chose the wrong option')

        if to_add == 1:
            self.add_client()
        else:
            print("Maybe another time")

        self.shows_the_details_clients(clients)

    def edit_client(self):
        clients = self.get_clients_by_input_last_name()

        if not clients:
            raise WrongOptionException("No client in the database")

        self.shows_the_details_clients(clients)

        client = self.client_select()
        if client not in clients:
            raise WrongOptionException('You selected the wrong client id')

        print("What do you want to edit: ")
        try:
            option = int(input("1 - First name, 2 - Last name, 3 - Phone, 4 - Address: "))
        except ValueError:
            raise WrongOptionException('You chose the wrong option')

        if 0 <= option < 4:
            try:
                field_name = ['first_name', 'last_name', 'phone'][option - 1]
            except IndexError:
                raise WrongOptionException('You chose the wrong option')

            self.set_client_detail(client, field_name)

        if option == 4:
            print("What do you want to edit: ")
            address = client.address
            try:
                option_address = int(input("1 - Edit street, 2 - Edit street number, 3 - Edit apartment number, "
                                           "4 - Edit zipcode, 5 - Edit city: "))
            except ValueError:
                raise WrongOptionException('You chose the wrong option')

            try:
                field_name = ['street', 'street_number', 'apartment_number', 'zipcode', 'city'][option_address - 1]
            except IndexError:
                raise WrongOptionException('You chose the wrong option')

            self.set_client_detail(address, field_name)

        if option > 4:
            print('You chose the wrong option')

    def delete_client(self):
        clients = self.get_clients_by_input_last_name()

        if not clients:
            raise WrongOptionException("No client in the database")

        self.shows_the_details_clients(clients)

        client = self.client_select()
        if client not in clients:
            raise WrongOptionException('You selected the wrong client id')

        self.client_db.remove_item_in_database(client)
        print("client removed")



