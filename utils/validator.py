import csv
import datetime
from typing import List

FILENAME_CSV = "client/wojewodztwa_miasta.csv"


class Validator:
    @staticmethod
    def is_valid_zipcode(zipcode: str) -> bool:
        return (
            len(zipcode) == 6 and
            zipcode[2] == "-" and
            zipcode[0:2].isdigit() and
            zipcode[3:].isdigit()
        )

    @staticmethod
    def get_cities_from_file(file_name: str) -> List[str]:
        city_list = []
        with open(file_name) as file:
            readers = csv.reader(file, delimiter=';')
            for row in readers:
                city = row[1]
                city_list.append(city)

        return city_list

    @staticmethod
    def is_valid_date(date_string: str) -> bool:
        format_date = "%Y-%m-%d"
        try:
            datetime.datetime.strptime(date_string, format_date)
        except ValueError:
            return False
        else:
            return True

    @classmethod
    def is_valid_city(cls, valid_city: str) -> bool:
        return valid_city.title() in cls.get_cities_from_file(FILENAME_CSV)




