from exceptions import (
    InvalidLeaseContractData,
    ClientNotFound,
    WrongOptionException
)

from car.models import CarDatabase
from client.models import ClientDatabase

from lease_contract.models import (
    LeaseContract,
    LeaseContractDatabase
)


class LeaseContractMenu:

    def __init__(self, lc_db: LeaseContractDatabase, car_db: CarDatabase, client_db: ClientDatabase):
        self.lc_db = lc_db
        self.car_db = car_db
        self.client_db = client_db

    @staticmethod
    def shows_the_details_lease_contracts(lease_contracts):
        for contract in lease_contracts:
            print(contract.get_details())

    @staticmethod
    def set_lease_contract_detail(client, field):
        new_value = input(f"Give new {field}: ")
        setattr(client, field, new_value)  # zmienia wartość atrybutu obiektu

    def get_lease_contracts_by_input_last_name(self):
        last_name = input("Enter your last name: ")
        lease_contracts = self.lc_db.find_all_item_in_database(last_name)
        return lease_contracts

    def contract_select(self):
        try:
            contract_id = int(input("Enter the contract id to edit: "))
        except ValueError:
            pass
        else:
            contract = self.lc_db.get_item_by_id_in_database(contract_id)
            return contract

    def add_lease_contract(self):
        try:
            lease_contract = LeaseContract.create_lease_contract(self.car_db, self.client_db)
            print(lease_contract.get_details())
        except InvalidLeaseContractData:
            print('Cannot create a lease contract with provided data')
        except ClientNotFound:
            print('Cannot create a lease contract, chosen invalid client')
        else:
            self.lc_db.add_item(lease_contract)
            print("Lease contract added")

    def search_lease_contract(self):
        lease_contracts = self.get_lease_contracts_by_input_last_name()

        if not lease_contracts:
            raise WrongOptionException('You selected the wrong contract id')

        self.shows_the_details_lease_contracts(lease_contracts)

    def edit_lease_contract(self):
        lease_contracts = self.get_lease_contracts_by_input_last_name()

        if not lease_contracts:
            raise WrongOptionException("No lease_contract in the database")

        self.shows_the_details_lease_contracts(lease_contracts)

        contract = self.contract_select()
        if contract not in lease_contracts:
            raise WrongOptionException('You selected the wrong contract id')

        print("What do you want to edit: ")
        try:
            option = int(input("1 - date start, 2 - data end: "))
        except ValueError:
            raise WrongOptionException('You chose the wrong option')

        try:
            field_name = ['date_start', 'data_end'][option - 1]
        except IndexError:
            raise WrongOptionException('You chose the wrong option')

        self.set_lease_contract_detail(contract, field_name)

    def delete_lease_contract(self):
        lease_contracts = self.get_lease_contracts_by_input_last_name()

        if not lease_contracts:
            raise WrongOptionException("No lease_contract in the database")

        self.shows_the_details_lease_contracts(lease_contracts)

        contract = self.contract_select()
        if contract not in lease_contracts:
            raise WrongOptionException('You selected the wrong contract id')

        self.lc_db.remove_item_in_database(contract)
        print("Lease contract removed")






