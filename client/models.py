from typing import (
    List,
    Dict,
    Optional
)

from car_rent.address import Address
from car_rent.database import Database

FILENAME_JSON = "databases/client.json"


class Client:
    identifier = None

    def __init__(self, first_name, last_name, phone, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address

    def get_details(self) -> str:
        return ",".join([
            f"id: {self.identifier}",
            f"first_name: {self.first_name}",
            f"last_name: {self.last_name}",
            f"phone: {self.phone}",
            f"address: {self.address.get_details()}",
        ])

    def convect_to_dict(self) -> Dict:
        return {
            "id": self.identifier,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "address": self.address.convect_to_dict(),
        }

    @classmethod
    def create_client(cls, first_name: str = '', last_name: str = '', phone: str = '',
                      address: Optional[Address] = None) -> 'client':
        print("client data")
        while len(first_name) < 1 or first_name.isdigit():
            fist_name = input("Enter your first_name: ")

        while len(last_name) < 1 or last_name.isdigit():
            last_name = input("Enter your last_name: ")

        while len(phone) < 9 or not phone.isdigit():
            phone = input("Enter your phone number: ")

        print("client address data")
        if not address:
            address = Address.create_address()

        return cls(first_name.title(), last_name.title(), phone, address)

    def get_search_data(self):
        return self.last_name.lower()


class ClientDatabase(Database):
    database: List[Client]
    file_name = FILENAME_JSON

    def read_client_database(self):
        for client in self.read_content_from_file(self.file_name):
            address_client = client["address"]
            address = Address(
                address_client['street'],
                address_client['street_number'],
                address_client['apartment_number'],
                address_client['zipcode'],
                address_client['city']
            )

            new_client = Client(
                client["first_name"],
                client["last_name"],
                client["phone"],
                address,
            )

            self.add_item(new_client)













