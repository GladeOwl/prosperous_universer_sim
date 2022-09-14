import string
from logger import create_log, write_to_log, add_partition
from item import Item
from inventory import Inventory


class Production:
    def __init__(self, item: Item, inventory: Inventory) -> None:
        self.item: Item = item
        self.time: int = item.time
        self.time_left: int = item.time
        self.inventory: Inventory = inventory

    def tick(self, time: tuple):
        self.time_left -= 1
        if self.time_left <= 0:
            self.finish_production(time)

    def finish_production(self, time: tuple):
        write_to_log(
            time,
            self.item.producer,
            f"Produced: {self.item.name}, {self.item.produced_per_cycle} units",
        )
        self.time_left = self.time
        self.deposit_resources(time)

    def withdraw_resources(self, time: tuple):
        for item in self.item.reciepe:
            write_to_log(
                time,
                self.item.producer,
                f"Withdraw Request: {item['item'].name}, {item['amount']} units --> {self.current_production.name}",
            )
            self.inventory.remove_stock(item["item"], item["amount"])

    def deposit_resources(self, time: tuple):
        self.inventory.add_stock(self.item, self.item.produced_per_cycle, time)


class Producer:
    def __init__(
        self, name: string, queue: list, queue_slots: int, inventory: Inventory
    ) -> None:
        self.name: string = name
        self.queue: list = queue
        self.queue_slots = queue_slots
        self.inventory: Inventory = inventory
        self.current_production = []

    def tick(self, time: tuple):
        """Ticks the production by 1"""
        for production in self.current_production:
            production.tick(time)

    def initial_production(self):
        """Sets up the initial production queue for the Producer"""
        index = 0
        while index < self.queue_slots - len(self.current_production):
            self.setup_production()

    def next_production(self, production: Production):
        """Sets up the next production in the queue"""
        self.current_production.remove(production)
        print(self.name, len(self.current_production))
        self.setup_production()

    def setup_production(self):
        item = self.queue.pop(0)
        production = Production(item, self.inventory)
        self.current_production.append(production)
        self.queue.append(production)
