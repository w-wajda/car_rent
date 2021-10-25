from typing import (
    List,
    Dict
)

from database import Database

FILENAME_JSON = "databases/car.json"


class Car:
    identifier = None

    def __init__(self, brand, model, years, rental_price):
        self.brand = brand
        self.model = model
        self.years = years
        self.rental_price = rental_price

    def get_details(self) -> str:
        return ",".join([
            f"id: {self.identifier}",
            f"brand: {self.brand}",
            f"model: {self.model}",
            f"years: {self.years}",
            f"rental_price: {self.rental_price}",
        ])

    def convect_to_dict(self) -> Dict:
        return {
            "id": self.identifier,
            "brand": self.brand,
            "model": self.model,
            "years": self.years,
            "rental_price": self.rental_price,
        }

    @classmethod
    def create_car(cls, brand: str = '', model: str = '', years: str = '', rental_price: str = '') -> 'Car':

        while len(brand) == 0 or brand.isdigit():
            brand = input("Enter the brand: ")

        while len(model) == 0 or not brand.isalnum():
            model = input("Enter the model: ")

        while len(years) < 4 or years.isalpha():
            years = input("Enter the years: ")

        while len(rental_price) == 0 or rental_price.isalpha():
            rental_price = input("Enter the rental price: ")

        return cls(brand, model, years, rental_price)

    def get_search_data(self):
        return self.brand


class CarDatabase(Database):
    database: List[Car]
    file_name = FILENAME_JSON

    def read_car_database(self):
        for car in self.read_content_from_file(self.file_name):
            new_car = Car(
                car["brand"],
                car["model"],
                car["years"],
                car["rental_price"]
            )

            self.add_item(new_car)














