import datetime
from typing import (
    List,
    Dict,
)

from car_rent.client.models import Client, ClientDatabase
from car_rent.car.models import Car, CarDatabase
from car_rent.utils.validator import Validator
from car_rent.database import Database

from car_rent.exceptions import (
    InvalidLeaseContractData,
    ClientNotFound
)

FILENAME_JSON = "databases/lease_contract.json"


class LeaseContract:
    identifier = None

    def __init__(self, date_start, date_end, car: Car, client: Client):
        self.date_start = date_start
        self.date_end = date_end
        self.car = car
        self.client = client

    def get_details(self) -> str:
        return ",".join([
            f"id: {self.identifier}",
            f'date_start: {self.date_start}',
            f'date_end: {self.date_end}',
            f'all_price: {self.get_all_price_for_lease_contract()}',
            f'car: {self.car.get_details()}',
            f'client: {self.client.get_details()}',

        ])

    def convect_to_dict(self) -> Dict:
        return {
            "id": self.identifier,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "car_id": self.car.identifier,
            "client_id": self.client.identifier,
        }

    @classmethod
    def create_lease_contract(cls, car_db: CarDatabase, client_db: ClientDatabase, date_start: str = '',
                              date_end: str = '') -> 'LeaseContract':

        while not Validator.is_valid_date(date_start):
            date_start = input("Enter date start in the format YYYY-MM-DD: ")

        while not Validator.is_valid_date(date_end):
            date_end = input("Enter date end in the format YYYY-MM-DD: ")

        car_db.show_all_items()

        car_id = input("Enter the id of the car to be rented or '+' if you want to add a new car: ")
        if car_id == "+":
            car = Car.create_car()
            car_db.add_item(car)
        elif car_id.isdigit():
            car_id = int(car_id)
            car = car_db.get_item_by_id_in_database(car_id)
        else:
            raise InvalidLeaseContractData()

        client = None

        contract_client = input("Enter the last name a loyal client or '+' if you want to add a new client: ")

        if contract_client == "+":
            client = Client.create_client()
            client_db.add_item(client)

        elif contract_client:
            clients = client_db.find_all_item_in_database(contract_client)

            for search_client in clients:
                print(search_client.get_details())

            client_id = int(input("Enter the id client: "))

            for temporary_client in clients:
                if temporary_client.identifier == client_id:
                    client = temporary_client

        if not client:
            raise ClientNotFound()

        lease_contract = cls(date_start, date_end, car, client)
        return lease_contract

    def get_all_price_for_lease_contract(self) -> int:
        format_date = "%Y-%m-%d"
        date_start = datetime.datetime.strptime(self.date_start, format_date)
        date_end = datetime.datetime.strptime(self.date_end, format_date)

        delta = date_end - date_start
        all_price = int(self.car.rental_price) * delta.days
        return all_price

    def get_search_data(self):
        return self.client.last_name


class LeaseContractDatabase(Database):
    database: List[LeaseContract]
    file_name = FILENAME_JSON

    def __init__(self):
        super().__init__()
        self.client_database = ClientDatabase()
        self.client_database.read_client_database()
        self.car_database = CarDatabase()
        self.car_database.read_car_database()

    def read_lease_contract_database(self):
        for lease_contract in self.read_content_from_file(self.file_name):
            client = self.client_database.get_item_by_id_in_database(lease_contract["client_id"])
            car = self.car_database.get_item_by_id_in_database(lease_contract["car_id"])

            new_lease_contract = LeaseContract(
                lease_contract["date_start"],
                lease_contract["date_end"],
                car,
                client,
            )

            self.add_item(new_lease_contract)














