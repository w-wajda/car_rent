from typing import Dict

from utils.validator import Validator


class Address:

    def __init__(self, street, street_number, apartment_number, zipcode, city):
        self.street = street
        self.street_number = street_number
        self.apartment_number = apartment_number
        self.zipcode = zipcode
        self.city = city

    def get_details(self) -> str:
        return ','.join([
            self.street,
            self.street_number,
            self.apartment_number,
            self.zipcode,
            self.city],
        )

    def convect_to_dict(self) -> Dict:
        return {
            "street": self.street,
            "street_number": self.street_number,
            "apartment_number": self.apartment_number,
            "zipcode": self.zipcode,
            "city": self.city,
        }

    @classmethod
    def create_address(
            cls, street: str = '', street_number: str = '', apartment_number: str = '', zipcode: str = '',
            city: str = '') -> 'Address':
        option = input("1 - flat, 2 - house: ")

        while len(street) == 0 or street.isdigit():
            street = input("Enter the street: ")

        while len(street_number) == 0 or not street_number.isalnum():
            street_number = input("Enter the street number: ")

        if option == 1:
            while len(apartment_number) == 0 or apartment_number.isalpha():
                apartment_number = input("Enter the apartment number: ")

        while not Validator.is_valid_zipcode(zipcode):
            zipcode = input("Enter the zipcode: ")

        while not Validator.is_valid_city(city):
            city = input("Enter the city: ")

        return cls(street.title(), street_number, apartment_number, zipcode, city.title())



