import csv
import json
from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import List


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
        products = [Product(**item) for item in data]
        return products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path) as file:
            data = csv.DictReader(file)
            products = [Product(**item) for item in data]
        return products
