import string
from logger import create_log, write_to_log, add_partition
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

    def tick(self, time: tuple):
        self.current_time -= 1
        if self.current_time <= 0:
            self.complete_production(time)

    def complete_production(self, time: tuple):
        write_to_log(
            f"[{time[0]}D:{time[1]}H:{time[2]}M] [{self.name}] Production Complete: {self.current_production.name}, Produced: {self.current_production.produced_per_cycle}"
        )
        self.deposit_resources(time)

        if self.current_production_index + 1 >= len(self.queue):
            self.current_production_index = 0
        else:
            self.current_production_index += 1

        self.current_production = self.queue[self.current_production_index]

        self.current_time = self.current_production.time
        self.withdraw_resources(time)

    def withdraw_resources(self, time: tuple):
        for item in self.current_production.reciepe:
            self.inventory.remove_stock(item["item"], item["amount"], time)

    def deposit_resources(self, time: tuple):
        self.inventory.add_stock(
            self.current_production, self.current_production.produced_per_cycle, time
        )
