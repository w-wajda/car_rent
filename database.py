import json
from json import JSONDecodeError
from typing import (
    List,
    Dict
)


class Database:
    file_name: str

    def __init__(self):
        self.database = []

    def add_item(self, new_item):
        existing_identifier = 0

        for item in self.database:
            if existing_identifier < item.identifier:
                existing_identifier = item.identifier

        next_identifier = existing_identifier + 1
        new_item.identifier = next_identifier

        self.database.append(new_item)

    def show_all_items(self):
        for items in self.database:
            print(items.get_details())

    @staticmethod
    def convert_to_json(obj) -> str:
        return json.dumps(obj, ensure_ascii=False, indent=4)

    @staticmethod
    def read_json(obj) -> List[Dict]:
        return json.loads(obj, ensure_ascii=False, indent=4)

    @staticmethod
    def read_content_from_file(file_name) -> List:
        with open(file_name) as file:
            try:
                content = json.load(file)
                return content
            except JSONDecodeError:
                return []

    @staticmethod
    def write_content_to_file(file_name, content):
        with open(file_name, "w") as f:
            f.write(content + "\n")

    def save_database(self):
        data_dict = [item.convect_to_dict() for item in self.database]
        record = self.convert_to_json(data_dict)
        self.write_content_to_file(self.file_name, record)

    def get_item_by_id_in_database(self, identifier):
        for item in self.database:
            if item.identifier == identifier:
                return item

    def remove_item_in_database(self, item_to_remove):
        self.database = [item for item in self.database if item is not item_to_remove]

    def find_all_item_in_database(self, lookup_item):
        return [item for item in self.database if item.get_search_data().lower() == lookup_item.lower()]



