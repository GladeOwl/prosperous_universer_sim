import string
from logger import create_log, write_to_log, add_partition
from item import Item
from inventory import Inventory


class Producer:
    def __init__(
        self, name: string, queue: list, queue_slots: int, inventory: Inventory
    ) -> None:
        self.name: string = name
        self.queue: list = queue
        self.queue_slots = queue_slots
        self.inventory: Inventory = inventory
        self.current_production = []

    def setup_production(self):
        for index in range(self.queue_slots - len(self.current_production)):
            item = self.queue.pop(0)
            production = Production(item, self.inventory)
            self.current_production.append(production)
            self.queue.append(production)

    def tick(self, time: tuple):
        """Ticks the production by 1"""
        for production in self.current_production:
            production.tick()

    def complete_production(self, time: tuple):
        """Completes the production of an item"""
        self.deposit_resources(time)

        if self.current_production_index + 1 >= len(self.queue):
            self.current_production_index = 0
        else:
            self.current_production_index += 1

        self.current_production = self.queue[self.current_production_index]

        self.current_time = self.current_production.time
        self.withdraw_resources(time)

    def withdraw_resources(self, time: tuple):
        """Witdraws the required resources from the inventory"""
        for item in self.current_production.reciepe:
            self.inventory.remove_stock(item["item"], item["amount"], time)

    def deposit_resources(self, time: tuple):
        """Desposits the resources to the inventory"""
        self.inventory.add_stock(
            self.current_production, self.current_production.produced_per_cycle, time
        )


class Production:
    def __init__(self, item: Item, inventory: Inventory) -> None:
        self.item: Item = item
        self.time: int = item.time
        self.time_left = item.time
        self.inventory: Inventory = inventory

    def tick(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.finish_production()

    def finish_production(self, time: tuple):
        write_to_log(
            time,
            self.item.producer,
            f"Produced: {self.current_production.name}, {self.current_production.produced_per_cycle} units",
        )
        self.deposit_resources()

    def withdraw_resources(self, time: tuple):
        write_to_log(
            time,
            self.item.producer,
            f"Withdraw Request: {item['item'].name}, {item['amount']} units --> {self.current_production.name}",
        )
        for item in self.item.reciepe:
            self.inventory.remove_stock(item["item"], item["amount"])

    def deposit_resources(self):
        self.inventory.add_stock(self.item, self.item.produced_per_cycle)
