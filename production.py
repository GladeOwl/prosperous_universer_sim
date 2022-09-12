import string
from item import Item
from inventory import Inventory


class Producer:
    def __init__(self, name: string, queue: list, inventory: Inventory) -> None:
        self.name: string = name
        self.queue: list = queue
        self.inventory: Inventory = inventory
        self.current_production_index: int = 0
        self.current_production: Item = self.queue[self.current_production_index]
        self.current_time: int = self.current_production.time

    def tick(self):
        self.current_time -= 1
        if self.current_time <= 0:
            self.complete_production()

    def complete_production(self):
        print(
            f"Production Complete: {self.current_production.name}, Produced: {self.current_production.produced_per_cycle}"
        )
        self.deposit_resources()

        if self.current_production_index >= len(self.queue):
            self.current_production_index += 1
        else:
            self.current_production_index = 0

        self.current_production = self.queue[self.current_production_index]

    def withdraw_resources(self):
        for item in self.current_production.reciepe:
            self.inventory.remove_stock(item["item"], item["amount"])

    def deposit_resources(self):
        self.inventory.add_stock(
            self.current_production, self.current_production.produced_per_cycle
        )
