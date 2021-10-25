from car.models import (
    Car,
    CarDatabase,
)
from exceptions import WrongOptionException


class CarMenu:
    """ TODO: zrobić mixiny per add, search itp."""

    def __init__(self, car_db: CarDatabase):
        self.car_db = car_db

    @staticmethod
    def shows_the_details_of_the_cars(cars):
        for car in cars:
            print(car.get_details())

    @staticmethod
    def set_car_detail(car, field):
        new_value = input(f"Give new {field}: ")
        setattr(car, field, new_value)  # zmienia wartość atrybutu obiektu

    def get_cars_by_input_brand(self):
        give_brand = input("Enter the brand: ")
        cars = self.car_db.find_all_item_in_database(give_brand)
        return cars

    def car_select(self):
        try:
            car_id = int(input("Enter the car id to edit: "))
        except ValueError:
            pass
        else:
            car = self.car_db.get_item_by_id_in_database(car_id)
            return car

    def add_car(self):
        car = Car.create_car()
        self.car_db.add_item(car)
        print("Car added")

    def search_car(self):
        cars = self.get_cars_by_input_brand()

        if not cars:
            raise WrongOptionException("No car in the database")

        try:
            to_add = int(input("Do you want add a car? 1  - YES, 2 - NO: "))
        except ValueError:
            raise WrongOptionException('You chose the wrong option')

        if to_add == 1:
            self.add_car()
        else:
            print("Maybe another time")

        self.shows_the_details_of_the_cars(cars)

    def edit_car(self):
        cars = self.get_cars_by_input_brand()

        if not cars:
            raise WrongOptionException("No car in the database")

        self.shows_the_details_of_the_cars(cars)

        car = self.car_select()
        if car not in cars:
            raise WrongOptionException('You selected the wrong car id')

        print("What do you want to edit: ")
        try:
            option = int(input("1 - Brand, 2 - Model, 3 - Years, 4 - Rental price: "))
        except ValueError:
            raise WrongOptionException('You chose the wrong option')

        try:
            field_name = ['brand', 'model', 'years', 'rental_price'][option - 1]
        except IndexError:
            raise WrongOptionException('You chose the wrong option')

        self.set_car_detail(car, field_name)

    def delete_car(self):
        cars = self.get_cars_by_input_brand()

        if not cars:
            raise WrongOptionException("No car in the database")

        self.shows_the_details_of_the_cars(cars)

        car = self.car_select()
        if car not in cars:
            raise WrongOptionException('You selected the wrong car id')

        self.car_db.remove_item_in_database(car)
        print("Car removed")




